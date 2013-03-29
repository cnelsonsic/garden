import random

from resources.currencies import CURRENCIES
from savegame import Saveable

class Player(Saveable):
    def __init__(self):
        self.currency = random.choice(CURRENCIES)
        self.money = 0
        self.ticks = 0
        self.inventory = [] # The player's inventory contents

    def tick(self):
        self.ticks += 1
