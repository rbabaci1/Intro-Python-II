from colorama import Fore, Back

from texts import playerNameText, optionsText, selectOptionText, welcomeMessage,  playerWinsText
from item import Item
from player import Player
from room import Room
from lightSource import LightSource

###########################################################################
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", False, [Item("sandels"), Item("oranges")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True, [Item("batteries"), Item("hummer")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False, [Item("cable"), Item("jacket"), LightSource("lamp")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", True, [Item("hat"), Item("jeans")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False, [Item("lamborghini"), Item("diammons"), Item("gold")]),
}

###########################################################################
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

###########################################################################


def getPlayerInput():
    return input(selectOptionText).lower().split()


###########################################################################
player_name = input(playerNameText)
player = Player(player_name, room["outside"])
print(welcomeMessage)
print(Back.RESET + Fore.BLUE + optionsText)

###########################################################################
playerInput = ""
while True:
    print(Fore.RESET + f"{player.current_room.display(player.inventory)}")
    playerInput = getPlayerInput()
    print(Fore.BLUE + "[i/inventory] Carried items  |  [o] Options")

    if len(playerInput) == 1:
        if playerInput[0] == "q":
            break
        elif player.current_room.name == "Treasure Chamber":
            print(playerWinsText)
            break
        else:
            player.manageVerb(playerInput[0])

    elif len(playerInput) == 2:
        player.manageNoun(playerInput)

print(Back.RESET + Fore.GREEN + "\n\t*** Good bye " + Fore.WHITE +
      f"{player_name}" + Fore.GREEN + ", see you next time. ***\n")
