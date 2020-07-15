# Implement a class to hold room information. This should have name and
# description attributes.
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
        else:
            return self.w_to
