from room import Room
from player import Player
import textwrap
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
player = Player("Rabah", room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = {"n": "n_to", "s": "s_to", "e": "e_to", "w": "w_to"}
userInput = None

while True:
    current_room = player.location
    print(f"\nYou are in the \"{current_room.name}\" room.")
    print(f"Description: \"{current_room.description}\".")
    userInput = input(
        "\nPlease select your next room direction:\n`north`\t`south`\t`east`\t`west`\n  [n]\t  [s]\t  [e]\t  [w]\n\n>>> ")
    if userInput is "q":
        break
    elif userInput not in directions:
        print("\t\n*** Direction not allowed. Try again? ***")
    else:
        if (hasattr(current_room, directions[userInput])):
            player.location = current_room.getNextRoom(userInput)
        else:
            print(
                "\n*** No room is available in that direction. Try a different direction. ***\n")

print("\t*** Good bye, see you next time. ***")
