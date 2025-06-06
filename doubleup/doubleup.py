#!/usr/bin/env python3

from itertools import product
import math

def get_prob(dmg1, dmg2, hp, recovery=0):
    """
    Returns the probability that the defender is KO'd by two hits,
    accounting for possible HP recovery between hits.

    :param dmg1: list of 16 ints, damage rolls from attack 1
    :param dmg2: list of 16 ints, damage rolls from attack 2
    :param hp: int, defender's starting HP
    :param recovery: int, HP recovered between hits (default = 0)
    :return: float, KO probability
    """
    assert len(dmg1) == 16 and len(dmg2) == 16, "Both damage lists must have 16 values"

    ko = 0
    for d1, d2 in product(dmg1, dmg2):
        if d1 + d2 >= hp + recovery:
            ko += 1

    return ko / 256

# Example usage
a1 = [140, 144, 144, 146, 146, 150, 150, 152, 156, 156, 158, 158, 162, 162, 164, 168]
#a2 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
hp = 257
rec = math.floor(hp/4)  # e.g. Sitrus Berry

prob = get_prob(a1, a1, hp, rec)
print(f"KO probability: {prob:.2%}")
