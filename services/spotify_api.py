# services/spotify_api.py

from utils.config import get_spotify_client

class SpotifyAPI:
    def __init__(self):
        self.sp = get_spotify_client()

    def get_current_user_top_tracks(self, limit=20, time_range='short_term'):
        return self.sp.current_user_top_tracks(limit=limit, time_range=time_range)

    def get_audio_features(self, track_ids):
        return self.sp.audio_features(track_ids)
