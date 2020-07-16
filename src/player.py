from colorama import Fore, Back


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    @property
    def roomItems(self):
        return self.current_room.items

    def walk(self, direction):
        try:
            nextRoom = self.current_room.getNextRoom(direction)
            if nextRoom == None:
                raise AttributeError
            else:
                self.current_room = nextRoom
                print(Fore.GREEN + "Moving...\n" +
                      Fore.RESET + f"{self.current_room}")
        except AttributeError:
            print(Back.RESET + Fore.RED +
                  f"**** There is no path in that direction! TRY AGAIN ****")

    def getItem(self, item):
        item = [i for i in self.roomItems if i.name == item]
        if len(item):
            self.inventory.append(item[0])
            item[0].on_take()
            self.roomItems.remove(item[0])
        else:
            print(
                Back.RESET + Fore.WHITE + f"{item}" + Fore.RED + " is not available in the current room. TRY A DIFFERENT ITEM.")

    def dropItem(self, item):
        items = [i for i in self.inventory if i.name == item]
        if len(items):
            self.roomItems.append(items[0])
            items[0].on_drop()
            del items[0]
        else:
            print(Back.RESET + Fore.WHITE +
                  f"{item}" + Fore.RED + " is not available in your inventory. TRY A DIFFERENT ITEM.")
