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
        items = [i for i in self.roomItems if i.name == item]
        if len(items):
            self.inventory.append(items[0])
            items[0].on_take()
            del items[0]
        else:
            print(
                f"{item} is not available in the current room. TRY A DIFFERENT ITEM.")

    def dropItem(self, item):
        items = [i for i in self.inventory if i.name == item]
        if len(items):
            self.roomItems.append(items[0])
            items[0].on_drop()
            del items[0]
        else:
            print(f"{item} is not available in your inventory. TRY A DIFFERENT ITEM.")
