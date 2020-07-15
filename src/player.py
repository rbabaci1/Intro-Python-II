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
        except AttributeError:
            print(f"\n**** There is no path in that direction! TRY AGAIN ****")

    def getItem(self, item):
        if item in self.roomItems:
            self.inventory.append(item)
            self.roomItems.remove(item)
        else:
            print(
                f"{item}'s not available in the current room. TRY A DIFFERENT ITEM")

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.roomItems.append(item)
        else:
            print(f"{item}'s not available in your inventory. TRY A DIFFERENT ITEM")
