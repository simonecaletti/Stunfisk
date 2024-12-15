#!/bin/python3

from structure.pokemon import Pokemon
from structure.damage import damage, damage_list


pkm1 = Pokemon("Chikorita", 50, ["Tackle"], None, None, [4,252,0,0,0,252], [31,31,31,31,31,31], "adamant", "fire")
pkm2 = Pokemon("Metapod", 50, ["Tackle"], None, None, [252,0,252,0,4,0], [31,31,31,31,31,31], "bold", "fire")

#check damage calc
dmg = damage(pkm1, pkm2, "Tackle")
print("dmg with roll: ", dmg)
dmgmin = damage(pkm1, pkm2, "Tackle", "min")
print("dmg min: ", dmgmin)
dmgmax = damage(pkm1, pkm2, "Tackle", "max")
print("dmg max: ", dmgmax)
dmgall = damage_list(pkm1, pkm2, "Tackle")
print("dmg rolls: ", dmgall)
print("\n")

#check stats calc
print("{}, lv ".format(pkm1.specie), pkm1.lv)
print(pkm1.stats)
print("{}, lv ".format(pkm2.specie), pkm2.lv)
print(pkm2.stats)


