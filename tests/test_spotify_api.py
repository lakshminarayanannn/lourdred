# tests/test_spotify_api.py

import unittest
from services.spotify_api import SpotifyAPI

class TestSpotifyAPI(unittest.TestCase):
    def setUp(self):
        self.spotify_api = SpotifyAPI()

    def test_get_current_user_top_tracks(self):
        top_tracks = self.spotify_api.get_current_user_top_tracks(limit=5)
        self.assertIsNotNone(top_tracks)
        self.assertTrue(len(top_tracks['items']) > 0)

    def test_get_audio_features(self):
        top_tracks = self.spotify_api.get_current_user_top_tracks(limit=5)
        track_ids = [track['id'] for track in top_tracks['items']]
        audio_features = self.spotify_api.get_audio_features(track_ids)
        self.assertEqual(len(audio_features), len(track_ids))
        for feature in audio_features:
            self.assertIsNotNone(feature)

if __name__ == '__main__':
    unittest.main()
