# models/song.py

class Song:
    def __init__(self, song_id, name, danceability, energy, valence, tempo, liveness, loudness):
        self.song_id = song_id
        self.name = name
        self.danceability = danceability
        self.energy = energy
        self.valence = valence
        self.tempo = tempo
        self.liveness = liveness
        self.loudness = loudness

    @classmethod
    def from_api_data(cls, audio_feature, track_name):
        return cls(
            song_id=audio_feature['id'],
            name=track_name,
            danceability=audio_feature['danceability'],
            energy=audio_feature['energy'],
            valence=audio_feature['valence'],
            tempo=audio_feature['tempo'],
            liveness=audio_feature['liveness'],
            loudness=audio_feature['loudness']
        )
