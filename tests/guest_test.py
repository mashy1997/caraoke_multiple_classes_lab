import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Bethany Musk", 22)

    def test_guest_has_name(self):
        self.guest.get_guest_name()

    def test_guest_has_age(self):
        self.guest.get_guest_age()

