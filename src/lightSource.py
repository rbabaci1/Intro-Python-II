from colorama import Fore

from item import Item


class LightSource(Item):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def on_drop():
        print(Fore.RED + "It's not wise to drop your source of light!" + Fore.RESET)
