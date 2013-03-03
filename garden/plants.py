'''A module for randomly generating plants.'''
import random
from random import randint, choice

from names import plant
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
    'This tree is roughly 136 cm tall by 12 cm wide. It has oval-shaped leaves, 1 cm wide by 4 cm long. The plant takes 50 days to reach maturity and begin flowering. It produces gray colored blooms, with a pungeant aroma. After flowering, it produces tangy fruit that is 2 cm wide by 2 cm long. In a growing season, it can produce anywhere from 1 to 5 fruit. The fruit takes 4 days to ripen fully from the day the bud first forms. Its seeds are roughly 0.7 cm wide by 5.5 cm long. They take 14 days to germinate.'
    >>> p = Plant(seed=1)
    >>> p.description()
    'This bush is roughly 101 cm tall by 47 cm wide. It has triangular-shaped leaves, 1 cm wide by 1 cm long. The plant takes 44 days to reach maturity and begin flowering. It produces saddle brown colored blooms, with a pungeant aroma. After flowering, it produces poisonous fruit that is 1 cm wide by 5 cm long. In a growing season, it can produce anywhere from 2 to 15 fruit. The fruit takes 22 days to ripen fully from the day the bud first forms. Its seeds are roughly 0.4 cm wide by 0.3 cm long. They take 17 days to germinate.'
    '''

    def __init__(self, name=None, seed=None):
        if seed:
            self.seed = seed
            random.seed(seed)

        if name:
            self.name = name
        else:
            self.name = plant(seed)

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
