import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Cuff it", "Beyonce", 3)

    def test_song_has_name(self):
        self.song.get_song_name()

    def get_song_artist(self):
        self.song.get_artist()

    def get_song_duration(self):
        self.song.get_song_duration()