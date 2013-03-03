'''A tiny module to generate names suitable for plants and animals.
Uses the same concept as hastebin, and indirectly as http://tools.arantius.com/password'''
import random

def plant(seed=None):
    """
    >>> plant(seed=1234)
    'Mayu'
    >>> plant(seed=1)
    'Wo'
    """
    return random_name(minlength=2, maxlength=4, seed=seed)

def animal(seed=None):
    """
    >>> animal(seed=1234)
    'Mayuqoco'
    """
    return random_name(minlength=4, maxlength=8, seed=seed)

def random_name(minlength=4, maxlength=10, seed=None):
    """
    >>> random_name(seed=1234)
    'Mayuqocoga'
    >>> random_name(minlength=4, maxlength=4, seed=1234)
    'Mayu'
    >>> random_name(minlength=14, maxlength=14, seed=1234)
    'Mayuqocogavero'
    >>> random_name(minlength=64, maxlength=64, seed=1234)
    'Mayuqocogaverofadanucimocihirikeyipanafikaqapayozajahufazawaleku'
    """
    if seed:
        random.seed(seed)

    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    length = random.randint(minlength, maxlength)
    name = ""
    for pos in range(length):
        for letter in random.choice(consonants if pos % 2 == 0 else vowels):
            name += letter
    return name.title()
