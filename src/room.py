from colorama import Fore, Back


class Room:
    def __init__(self, name, description, is_light, items=None):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        if items is None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        output = f"Current room: {self.name}\nDescription: {self.description}\nAvailable items: "
        return output + ("Nothing left" if len(self.items) == 0 else ",  ".join(i.name for i in self.items))
