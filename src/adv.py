import os, sys

from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    'a rusty bucket' : Item('a rusty bucket', "never underestimate the usefulness of a bucket"),

}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", items['a rusty bucket']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. """, "a useless penny"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "retro Air Jordans"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "Howard the Duck VHS tape"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "a spoon"),
}




# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']

room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']

room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']

room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



print('Welcome, lets play an adventure game!')
print('_____________________________________')
name = input("Enter your name\n")

player = Player(name, room['outside']) 

play = True

while play is not False:

    user_input = input(f'\nplease enter (n)orth, (s)outh, (e)ast, (w)est, or (q)uit\n >').lower()

    if user_input == 'n':
        player.direction(user_input)
        print(f'you have moved to {player.current_room}')
    elif user_input == 's':
        player.direction(user_input)
        print(f'you have moved to {player.current_room}')
    elif user_input == 'e':
        player.direction(user_input)
        print(f'you have moved to {player.current_room}')
    elif user_input == 'w':
        player.direction(user_input)
        print(f'you have moved to {player.current_room}')
    # elif user_input == 'g':
    #     print('item obtained')
    # elif user_input == 'd':
    #     print('item dropped')
    elif user_input == 'q':
        print('\nSee you next time!')
        play = False
    else:
        print('\nWrong answer try again')
    
    




    















    

    

    



