import textwrap

from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["sandels", "oranges"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["torch", "hummer"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["cable", "jacket"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["hat", "jeans"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["lamborghini", "diammons", "gold"]),
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
   { n } North | { s } South |  { w } West | { e } East\n
******************** Other Options ***************************
   { get 'item name' } | { take 'item name' } Carry an item
   { i } | { inventory } Show carried items
******************** Enter [Q] to Exit the Adventure *********\n>>> """
playerInput = ""

print(f"\n****** WELCOME TO THE GREAT ADVENTURE GAME *********")
while True:
    current_room = player.current_room
    print(f"You are in the \"{current_room.name}\" room.")
    print(f"Description: \"{current_room.description}\".")

    items = ""
    for i in current_room.items:
        items += "  {},".format(i)
    print("\nAvailable items to carry: {}\n".format(items))
    playerInput = input(instructional_text).lower().split()

    if len(playerInput) == 1:
        if playerInput[0] == "q":
            break
        elif playerInput[0] == "i" or playerInput[0] == "inventory":
            print(player.roomItems)
        else:
            player.walk(playerInput[0])
    if len(playerInput) == 2:
        if playerInput[0] != "get" and playerInput[0] != "take" and playerInput[0] != "drop":
            print(
                "To get you're wanted item, you must proceed with (get or take) + item name.\n")
        elif playerInput[0] == "drop":
            player.dropItem(playerInput[1])
        else:
            player.getItem(playerInput[1])


print(f"\t*** Good bye {player_name}, see you next time. ***")
