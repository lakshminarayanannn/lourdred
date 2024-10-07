# utils/config.py

import os
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:7777/callback'
SCOPE = 'user-top-read'

class Config:
    SPOTIFY_CLIENT_ID = CLIENT_ID
    SPOTIFY_CLIENT_SECRET = CLIENT_SECRET
    SPOTIFY_REDIRECT_URI = REDIRECT_URI
    SPOTIFY_SCOPE = SCOPE
    PAGE_TITLE = 'Spotify Song Analysis'
    PAGE_ICON = ':musical_note:'

def get_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=Config.SPOTIFY_CLIENT_ID,
        client_secret=Config.SPOTIFY_CLIENT_SECRET,
        redirect_uri=Config.SPOTIFY_REDIRECT_URI,
        scope=Config.SPOTIFY_SCOPE
    )
    return Spotify(auth_manager=auth_manager)
