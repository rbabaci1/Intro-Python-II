from colorama import Fore, Back

from item import Item
from player import Player
from room import Room
from lightSource import LightSource

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("sandels"), Item("oranges")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("batteries"), Item("hummer")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("cable"), Item("jacket"), LightSource("lamp")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("hat"), Item("jeans")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("lamborghini"), Item("diammons"), Item("gold")]),
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
player_name = input(
    Back.BLACK + Fore.YELLOW + "Enter Your character name to get started >>>" + Back.RESET + Fore.WHITE + " ")
player = Player(player_name, room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
options = """ ------------------ Available Move Options ---------------------
|   { n } North | { s } South |  { w } West | { e } East        |
|                                                               |   
 ------------------- Other Options -----------------------------
|   { get 'item name' } | { take 'item name' } To carry an item.|
|                                                               |
 --------------- { Q } to Exit the Adventure -------------------"""
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(Back.RESET + Fore.GREEN +
      f"\n****** WELCOME TO THE GREAT ADVENTURE GAME *********\n")
print(Fore.RESET + f"{player.current_room}")
print(Back.RESET + Fore.BLUE + options)

playerInput = ""
while True:
    playerInput = input(Back.BLACK + Fore.YELLOW +
                        "Select an option >>>" + Back.RESET + Fore.WHITE + " ").lower().split()
    print(Fore.BLUE +
          "[i/inventory] Carried items  |  [o] Options  |  [r] Room details")

    if len(playerInput) == 1:
        if playerInput[0] == "q":
            break
        elif playerInput[0] in ["i", "inventory"]:
            print("Empty." if len(player.inventory) ==
                  0 else ",  ".join(i.name for i in player.inventory))
        elif playerInput[0] == "o":
            print(Fore.BLUE + options)
        elif playerInput[0] == "r":
            print(Fore.WHITE + f"{player.current_room}")
        else:
            player.walk(playerInput[0])
            if player.current_room.name == "Treasure Chamber":
                print(Fore.BLACK + Back.GREEN +
                      "\n*** Congrats, you made it to the Treasure room. All the left items are yours. ***\n")
                break
    elif len(playerInput) == 2:
        if playerInput[0] not in ["get", "take", "drop"]:
            print(
                Fore.RED + "To get you're wanted item, you must proceed with (get or take) + item name.")
        elif playerInput[0] == "drop":
            player.dropItem(playerInput[1])
        else:
            player.getItem(playerInput[1])


print(Back.RESET + Fore.GREEN +
      "\n\t*** Good bye " + Fore.WHITE + f"{player_name}" + Fore.GREEN + ", see you next time. ***\n")
