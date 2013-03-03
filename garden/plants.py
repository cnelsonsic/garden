'''A module for randomly generating plants.'''
import random
from random import randint, choice

from resources.colors import COLORS

SHAPES = ("bush", "tree", "shrub")
LEAVES = ("oval", "needle", "triangular")
FRUITS = ("firm", "juicy", "hard", "soft", "dry", "tangy", "poisonous",
          "savory", "sweet")
SMELLS = ("pleasant", "pungeant", "rotten")

class Plant(object):
    '''
    >>> p = Plant(seed=1234)
    >>> p.description()
    'This shrub is roughly 90 cm tall by 4 cm wide. It has triangular-shaped leaves, 3 cm wide by 3 cm long. The plant takes 56 days to reach maturity and begin flowering. It produces burlywood colored blooms, with a rotten aroma. After flowering, it produces hard fruit that is 1 cm wide by 8 cm long. In a growing season, it can produce anywhere from 4 to 7 fruit. The fruit takes 11 days to ripen fully from the day the bud first forms. Its seeds are roughly 1.9 cm wide by 1.2 cm long. They take 1 days to germinate.'
    >>> p = Plant(seed=1)
    >>> p.description()
    'This bush is roughly 170 cm tall by 78 cm wide. It has needle-shaped leaves, 2 cm wide by 3 cm long. The plant takes 25 days to reach maturity and begin flowering. It produces plum colored blooms, with a pleasant aroma. After flowering, it produces firm fruit that is 9 cm wide by 5 cm long. In a growing season, it can produce anywhere from 1 to 4 fruit. The fruit takes 23 days to ripen fully from the day the bud first forms. Its seeds are roughly 2.3 cm wide by 9.5 cm long. They take 28 days to germinate.'
    '''

    def __init__(self, seed=None):
        if seed:
            self.seed = seed
            random.seed(seed)

        self.plant_shape = choice(SHAPES)
        self.plant_height = randint(4, 200)
        self.plant_width = randint(4, 100)
        self.plant_days = randint(14, 60)

        self.leaf_shape = choice(LEAVES)
        self.leaf_width = randint(1, 4)
        self.leaf_length = randint(1, 4)

        self.flower_color = choice(COLORS)
        self.flower_smell = choice(SMELLS)

        self.fruit_description = choice(FRUITS)
        self.fruit_width = randint(1, 10)
        self.fruit_length = randint(1, 10)
        self.fruit_days = randint(1, 30)
        self.fruit_min = randint(1, 5)
        self.fruit_max = randint(self.fruit_min, self.fruit_min*randint(2, 8))

        self.seed_width = randint(1, 100)/10.0
        self.seed_length = randint(1, 100)/10.0
        self.seed_days = randint(1, 30)


    def description(self):
        '''Return an imagination-sparking description for this plant.'''

        return ("This {plant_shape} is roughly {plant_height} cm tall "
                "by {plant_width} cm wide. "
                "It has {leaf_shape}-shaped leaves, "
                "{leaf_width} cm wide by {leaf_length} cm long. "
                "The plant takes {plant_days} days to reach maturity "
                "and begin flowering. "
                "It produces {flower_color} colored blooms, "
                "with a {flower_smell} aroma. "
                "After flowering, it produces {fruit_description} fruit "
                "that is {fruit_width} cm wide by {fruit_length} cm long. "
                "In a growing season, it can produce anywhere "
                "from {fruit_min} to {fruit_max} fruit. "
                "The fruit takes {fruit_days} days to ripen fully "
                "from the day the bud first forms. "
                "Its seeds are roughly {seed_width} cm wide "
                "by {seed_length} cm long. "
                "They take {seed_days} days to germinate."
                ).format(**self.__dict__)
