import textwrap

from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Sandels", "Oranges"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["Torch", "Hummer"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Cable", "Jacket"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["Hat", "Jeans"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["Lamborghini", "Diammons", "Gold"]),
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
player_name = input("Enter Your character name to get started >>> ")
player = Player(player_name, room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
instructional_text = """******************** Available Move Options ******************
**** { N } North | { S } South |  { W } West | { E } East ****
************** Enter [Q] to Exit the Adventure ***************\n>>> """
playerInput = ""

print("****** WELCOME TO THE GREAT ADVENTURE GAME *********")
while True:
    current_room = player.current_room
    print(f"\nYou are in the \"{current_room.name}\" room.")
    print(f"Description: \"{current_room.description}\".")

    items = ""
    for i in current_room.list:
        items += "  {},".format(i)
    print("Available items to grab: {}\n".format(items))
    playerInput = input(instructional_text).upper().split()

    if len(playerInput) == 1:
        if playerInput[0] == "Q":
            break
        else:
            player.walk(playerInput[0].lower())
    if len(playerInput) == 2:
        if playerInput[0] != "get" and playerInput[0] != "take" and playerInput[0] != "drop":
            print(
                "To get you're wanted item, you must proceed with (get or take) + item name.\n")
        elif playerInput[0] == "drop":
            if playerInput[1] in player.list:
                current_room.addItem(playerInput[1])
                player.removeItem(playerInput[1])
                print("\nItem dropped\n")
            else:
                print("\nThe selected item doesn't exists in your inventory.")
        else:
            if playerInput[1] in current_room.list:
                player.addItem(playerInput[1])
                current_room.removeItem(playerInput[1])
                print("\nItem added\n")
            else:
                print("The selected item doesn't exists in the current room.")

print("\t*** Good bye, see you next time. ***")
