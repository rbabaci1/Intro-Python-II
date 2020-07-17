from colorama import Fore, Back
from texts import optionsText
from validate import Validate


class Player(Validate):
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    @property
    def roomItems(self):
        return self.current_room.items

    def manageVerb(self, verb):
        if verb in ["i", "inventory"]:
            inv = "Empty." if len(self.inventory) == 0 else ",  ".join(
                i.name for i in self.inventory)
            print(Fore.MAGENTA + f"Inventory: {inv}")
        elif verb == "o":
            print(Fore.BLUE + options)
        else:
            self.walk(verb)

    def manageNoun(self, playerInput):
        if playerInput[0] not in ["get", "take", "drop"]:
            print(
                Fore.RED + "To get you're wanted item, you must proceed with (get or take) + item name.")
        elif playerInput[0] == "drop":
            self.dropItem(playerInput[1])
        else:
            self.getItem(playerInput[1])

    def walk(self, direction):
        result = self.validateDirection(direction)
        if result:
            self.current_room = result
        else:
            print(Back.RESET + Fore.RED + f"*** Direction blocked! TRY AGAIN ***")

    def getItem(self, item):
        result = self.validateItem(item, "room")
        if result:
            self.inventory.append(result)
            result.on_take()
            self.roomItems.remove(result)
        else:
            print(
                Back.RESET + Fore.MAGENTA + f"{item}" + Fore.RED + " is not available in the current room. TRY A DIFFERENT ITEM.")

    def dropItem(self, item):
        result = self.validateItem(item, "inventory")
        if result:
            self.roomItems.append(result)
            result.on_drop()
            self.inventory.remove(result)
        else:
            print(Back.RESET + Fore.WHITE +
                  f"{item}" + Fore.RED + " is not available in your inventory. TRY A DIFFERENT ITEM.")
