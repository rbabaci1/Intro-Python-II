class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.list = []

    def addItem(self, item):
        self.list.append(item)
