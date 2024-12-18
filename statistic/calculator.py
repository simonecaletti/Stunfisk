#!/bin/python3

#from structure.pokemon import update_hp
import itertools

def check_ko(pkm, dmg):
    if pkm.currentHP <= dmg:
        return True
    else:
        return False

def apply_dmg(pkm, dmg):
    if check_ko(pkm, dmg):
        pkm.update_hp(0)
    else:
        new_hp = pkm.currentHP - dmg
        pkm.update_hp(new_hp)
    return None

def count_nhko(hp, dmgmax):
    i = 0
    while hp > 0:
        hp -= dmgmax
        i +=1
    return i

def get_probability_nhko(hp, dmg_list):
    ikill = 0
    n = count_nhko(hp, dmg_list[-1])
    scenarios = list(itertools.product(dmg_list, repeat=n))
    for el  in scenarios:
        tot = sum(list(el))
        if (hp - tot) <= 0:
            ikill += 1
    prob = ikill/len(scenarios)
    return prob





