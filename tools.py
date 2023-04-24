import random


def rng(num):
    return random.randint(1, num)


def first(iterable, default=None):
    for item in iterable:
        return item
    return default