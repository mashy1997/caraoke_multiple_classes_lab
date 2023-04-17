import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Poptacular!", "pop")

    def test_room_has_name(self):
        self.room.get_room_name()

    def test_get_genre(self):
        self.room.get_genre()

    def test_guests_start_empty(self):
        self.assertEqual(0, self.room.number_of_guests())

    def test_can_check_in_guests(self):
        guest = Guest("Bethany Musk", 22)
        self.room.check_in_guests(guest)
        self.assertEqual(1, self.room.number_of_guests())

    def test_can_check_out_guests(self):
        guest = Guest("Bethany Musk", 22)
        self.room.check_in_guests(guest)
        self.room.check_out_guests(guest)
        self.assertEqual(0, self.room.number_of_guests())

    def test_songs_start_empty(self):
        self.assertEqual(0, self.room.number_of_songs())

    def test_adds_songs_to_room(self):
        song = Song("Cuff it", "Beyonce", 3)
        self.room.add_songs_to_room(song)
        self.assertEqual(1, self.room.number_of_songs())

