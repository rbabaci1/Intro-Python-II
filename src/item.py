from colorama import Fore, Back


class Item:
    def __init__(self, name, description="None"):
        self.name = name
        self.description = description

    def on_take(self):
        print(Back.RESET + Fore.GREEN +
              "You have picked up [{}].".format(self.name))

    def on_drop(self):
        print(Back.RESET + Fore.GREEN +
              "You have dropped [{}].".format(self.name))
