# app/main.py

import streamlit as st
import pandas as pd
from services.spotify_api import SpotifyAPI
from models.song import Song
from models.user import User
from utils.config import Config
from app.components.charts import render_bar_chart, render_tempo_gauge, render_line_chart

def main():
    st.set_page_config(page_title=Config.PAGE_TITLE, page_icon=Config.PAGE_ICON, layout="wide")
    
    st.markdown(
        """
        <style>
        /* Adjust the main content padding */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 4rem;
            padding-right: 4rem;
        }

        /* Ensure Plotly charts take full width */
        .stPlotlyChart {
            width: 100% !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Analysis for your Top Songs')
    st.write('Discover insights about your Spotify listening habits.')

    spotify_api = SpotifyAPI()

    try:
        top_tracks = spotify_api.get_current_user_top_tracks(limit=20, time_range='short_term')
    except Exception as e:
        st.error(f"Error fetching top tracks: {e}")
        return

    track_ids = [track['id'] for track in top_tracks['items']]
    audio_features = spotify_api.get_audio_features(track_ids)

    user = User(user_id='current_user', username='Spotify User')  # Replace with actual user data if available

    songs = []
    for track, audio in zip(top_tracks['items'], audio_features):
        if audio:  
            song = Song.from_api_data(audio, track['name'])
            user.add_song_to_history(song)
            songs.append(song)

    data = {
        'Track Name': [song.name for song in songs],
        'Tempo': [song.tempo for song in songs],
        'Danceability': [song.danceability for song in songs],
        'Liveness': [song.liveness for song in songs],
        'Loudness': [song.loudness for song in songs]
    }
    df = pd.DataFrame(data)
    df.set_index('Track Name', inplace=True)

    st.subheader('Audio Features for Top Tracks')

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.subheader('Tempo')
        render_tempo_gauge(df[['Tempo']])

    with col2:
        st.subheader('Danceability')
        render_bar_chart(df[['Danceability']])

    with col3:
        st.subheader('Liveness')
        render_bar_chart(df[['Liveness']])

    with col4:
        st.subheader('Loudness')
        render_line_chart(df[['Loudness']])

    st.markdown("<br><br>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
