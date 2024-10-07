# app/components/navigation.py

import streamlit as st

def navigation():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "User History", "Top K Songs", "Playlists", "Analysis", "Song Metadata"])
    return page
