class Validate():
    def validateDirection(self, direction):
        try:
            nextRoom = getattr(self.current_room, f"{direction}_to")
            if nextRoom == None:
                raise AttributeError
            else:
                return nextRoom
        except AttributeError:
            return False

    def validateItem(self, item, location):
        items = []
        if location == "room":
            items = [i for i in self.roomItems if i.name == item]
        else:
            items = [i for i in self.inventory if i.name == item]
        if len(items):
            return items[0]
        else:
            return False
