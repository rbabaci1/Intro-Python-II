class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

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
