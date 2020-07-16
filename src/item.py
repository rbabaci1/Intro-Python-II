class Item:
    def __init__(self, name, description="None"):
        self.name = name
        self.description = description

    def on_take(self):
        print("You have picked up {}.".format(self.name))

    def on_drop(self):
        print("You have dropped {}.".format(self.name))
