class Room:
    def __init__(self, name, description, list=None):
        self.name = name
        self.description = description
        if list is None:
            self.list = []
        else:
            self.list = list

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
