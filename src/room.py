from colorama import Fore, Back
from lightSource import LightSource


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

    def displayRoom(self, inventory):
        if self.is_light or any(isinstance(i, LightSource) == True for i in inventory):
            output = f"Current room: {self.name}\nDescription: {self.description}\nAvailable items: "
            return (output + (Fore.RED + "Nothing left" if len(self.items) == 0 else Fore.GREEN + ",  ".join(i.name for i in self.items)))
        else:
            return Fore.RED + "It's pitch black!, get a lamp to look around"
