class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        if items is None:
            self.items = []
        else:
            self.items = items

    def getNextRoom(self, userInput):
        if userInput == "n":
            return self.n_to
        elif userInput == "s":
            return self.s_to
        elif userInput == "e":
            return self.e_to
        elif userInput == "w":
            return self.w_to
        else:
            return None

    def addItem(self, item):
        self.list.append(item)

    def removeItem(self, item):
        self.list.remove(item)
