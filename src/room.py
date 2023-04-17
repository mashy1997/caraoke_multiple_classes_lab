class Room:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.guests = []
        self.songs = []

    def get_room_name(self):
        return self.name
    
    def get_genre(self):
        return self.genre
    
    def number_of_guests(self):
        return len(self.guests)
    
    def check_in_guests(self, guest_to_check_in):
        self.guests.append(guest_to_check_in)

    def check_out_guests(self, guest_to_check_out):
        self.guests.remove(guest_to_check_out)

    def number_of_songs(self):
        return len(self.songs)
    
    def add_songs_to_room(self, song_to_add):
        self.songs.append(song_to_add)