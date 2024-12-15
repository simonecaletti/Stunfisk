#!/bin/python3

#from structure.pokemon import update_hp

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

def count_nhko():
    return None

def get_probability():
    return None




