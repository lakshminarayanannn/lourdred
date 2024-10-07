# services/song_service.py

from typing import List, Dict
from services.spotify_api import SpotifyAPI
from models.song import Song

class SongService:
    def __init__(self, spotify_api: SpotifyAPI):
        self.spotify_api = spotify_api

    def search_songs(self, artist: str = None, genre: str = None, country: str = None, limit: int = 50) -> List[Song]:
        """
        Search for songs based on artist, genre, and country.

        :param artist: Artist name to search for.
        :param genre: Genre to filter songs.
        :param country: Country code to filter songs.
        :param limit: Number of songs to retrieve (max 100 per request).
        :return: List of Song objects.
        """
        query = []
        if artist:
            query.append(f'artist:{artist}')
        if genre:
            query.append(f'genre:{genre}')
        # Note: Spotify's Search API does not support genre filtering directly for tracks.
        # Genres can be used with recommendations or filter results manually.

        search_query = ' '.join(query) if query else 'year:2000-2023'  # Default query to get recent songs

        results = self.spotify_api.search_tracks(q=search_query, limit=limit, country=country)
        songs = []
        for item in results['tracks']['items']:
            song = Song(
                song_id=item['id'],
                name=item['name'],
                artists=[artist['name'] for artist in item['artists']],
                album=item['album']['name'],
                genre=genre,  # Genre needs to be inferred or handled separately
                danceability=None,  # To be filled if audio features are fetched
                energy=None,
                valence=None
            )
            songs.append(song)
        return songs

    def get_audio_features_for_songs(self, songs: List[Song]) -> None:
        """
        Populate audio features for each song in the list.

        :param songs: List of Song objects.
        """
        track_ids = [song.song_id for song in songs]
        audio_features = self.spotify_api.get_audio_features(track_ids)
        for song, features in zip(songs, audio_features):
            if features:
                song.danceability = features['danceability']
                song.energy = features['energy']
                song.valence = features['valence']
