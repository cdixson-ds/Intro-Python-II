from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

name = input("Enter your name\n")

player = Player(name, room['outside'])


while True:
    print(f"Current room: {player.room.name}\n {player.room.description}")

    player_input = input("Choose a direction, north, south, east or west: ").lower()

    if player_input == 'n' or player_input == 's' or player_input == 'e' or player_input == 'w' or player_input == 'q':
        if player_input == "n":
            player.room = player.room.n_to
        elif player_input == 's':
            player.room = player.room.s_to
        elif player_input == 'e':
            player.room = player.room.e_to
        elif player_input == 'w':
            player.room = player.room.w_to
        elif player_input == 'q':
            print('See you next time')
        break
    else:
        print("Enter a direction")



