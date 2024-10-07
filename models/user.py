# models/user.py

from models.song import Song

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.listening_history = []
        self.liked_playlists = []

    def add_song_to_history(self, song: Song):
        self.listening_history.append(song)

    def get_top_k_songs(self, k=10):
        # Simple frequency-based top K
        song_counts = {}
        for song in self.listening_history:
            song_counts[song.name] = song_counts.get(song.name, 0) + 1
        sorted_songs = sorted(song_counts.items(), key=lambda item: item[1], reverse=True)
        return sorted_songs[:k]
