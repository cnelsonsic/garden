'''Items are things that can be placed into a player's inventory.
'''

class Item(object):
    def __init__(self, name, value=0):
        self.name = name
        self.value = max(value, 1) # Worth at least one $CURRENCY

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
