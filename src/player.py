# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def direction(self, dir):
        loc = self.current_room.move(dir)

        if loc is not None:
            self.current_room = loc

        else:
            print('\nMovement not allowed')
            print('_______________________')

    def _str__(self):
        return f'{self.name}, you are currently in the {self.current_room}'



