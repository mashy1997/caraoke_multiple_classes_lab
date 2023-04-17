class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

    def get_song_name(self):
        return self.name
    
    def get_artist(self):
        return self.artist
    
    def get_song_duration(self):
        return self.duration