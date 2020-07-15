from room import Room
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["gold", "silver"]),

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
    current_room = player.current_room
    print(f"\nYou are in the \"{current_room.name}\" room.")
    print(f"Description: \"{current_room.description}\".")
    print(f"Available items: {current_room.list}")
    userInput = input(
        "\n1) To move to a different room select:\n  [n]\t  [s]\t  [e]\t  [w]\n`north`\t`south`\t `east`\t `west`\n\n2) [get/take item] to pick an item from the list:\n\n>>> ").split()
    print(userInput)

    if len(userInput) == 1:
        if userInput[0] == "q":
            break
        elif userInput[0] not in directions:
            print("\t\n*** Direction not allowed. Try again? ***")
        else:
            if (hasattr(current_room, directions[userInput[0]])):
                player.current_room = current_room.getNextRoom(userInput[0])
            else:
                print(
                    "\n*** No room is available in that direction. Try a different direction. ***\n")
    if len(userInput) == 2:
        if userInput[0] != "get" and userInput[0] != "take" and userInput[0] != "drop":
            print(
                "To get you're wanted item, you must proceed with (get or take) + item name.\n")
        elif userInput[0] == "drop":
            if userInput[1] in player.list:
                current_room.addItem(userInput[1])
                player.removeItem(userInput[1])
                print("\nItem dropped\n")
            else:
                print("\nThe selected item doesn't exists in your inventory.")
        else:
            if userInput[1] in current_room.list:
                player.addItem(userInput[1])
                current_room.removeItem(userInput[1])
                print("\nItem added\n")
            else:
                print("The selected item doesn't exists in the current room.")

print("\t*** Good bye, see you next time. ***")
