class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def walk(self, direction):
        nextRoom = getattr(self.current_room, f"{direction}_to")
        if nextRoom:
            self.current_room = nextRoom
        else:
            print(f"\nThere is no path in that direction! TRY AGAIN\n")

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
