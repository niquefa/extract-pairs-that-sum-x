import random
from analyzer import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    generated_set = set()
    while len(generated_set) < size:
        generated_set.add(random.choice([-1, 1]) * random.randint(0, limit))
    return list(generated_set)


def get_random_x(limit=constants.MAX_VALUE):
    return random.choice([-1, 1]) * random.randint(0, limit)
