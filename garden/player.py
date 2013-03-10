import random

from resources.currencies import CURRENCIES

class Player(object):
    def __init__(self):
        self.currency = random.choice(CURRENCIES)
        self.money = 0
        self.ticks = 0

    def tick(self):
        self.ticks += 1
