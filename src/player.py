class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def walk(self, direction):
        nextRoom = getattr(self.current_room, f"{direction}_to")
        if nextRoom:
            self.current_room = nextRoom
        else:
            print(f"\n**** There is no path in that direction! TRY AGAIN ****")

    def getItem(self, item):
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.items.remove(item)
        else:
            print(
                f"{item}'s not available in the current room. TRY A DIFFERENT ITEM")

    def dropItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.items.append(item)
        else:
            print(f"{item}'s not available in your inventory. TRY A DIFFERENT ITEM")
