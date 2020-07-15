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
            nextRoom = getattr(self.current_room, f"{direction}_to")
            self.current_room = nextRoom
            print(
                f"{self.current_room}\t\t\t\t\t\t[o] Options")
        except AttributeError:
            print(f"\n**** There is no path in that direction! TRY AGAIN ****")

    def getItem(self, item):
        try:
            self.roomItems.remove(item)
            self.inventory.append(item)
            print(f"You have picked up [ {item} ]")
        except ValueError:
            print(
                f"{item} is not available in the current room. TRY A DIFFERENT ITEM.")

    def dropItem(self, item):
        try:
            self.inventory.remove(item)
            self.roomItems.append(item)
            print(f"You have dropped [ {item} ]")
        except ValueError:
            print(f"{item} is not available in your inventory. TRY A DIFFERENT ITEM.")
