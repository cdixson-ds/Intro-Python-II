# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room
from item import Item



class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def direction(self, dir):
        loc = self.current_room.move(dir)

        if loc is not None:
            self.current_room = loc

        else:
            print('\nMovement not allowed')
            print('_______________________')

    def get_item(self, item):  #pass in name? or object?
        if len(self.current_room.inventory) > 0 and item in self.current_room.inventory:
            self.inventory.append(item)
            self.current_room.remove_item(item)  #define remove item in room class
            print(f'You picked up {item}')
        else:
            print('nothing to pick up')

    def drop_item(self, item):
        if len(self.inventory) > 0 and item in self.inventory:
            self.inventory.remove(item)
            self.current_room.add_item(item)
            print(f'{item} dropped')
        else:
            print('{item} not found')

    def _str__(self):
        return f'{self.name}, you are currently in the {self.current_room}'
