import random

from plants import Plant

class Store(object):
    '''Handles all the buying and selling.'''
    def __init__(self):
        self._inventory = []
        values = [10, ]
        for _ in range(1, 10):
            # Values like: 10, 21, 44, 90, 180 or 10, 20, 41, 82, 166
            values.append((max(values)*2) + random.randint(0, max(values)/10))

        for tier in range(0, 10):
            plant = Plant()
            plant.value = values[tier]
            self._inventory.append(plant)

    def get_inventory(self):
        return self._inventory
