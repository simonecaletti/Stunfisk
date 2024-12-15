#!/bin/python3

from structure.pokemon import Pokemon
from structure.damage import damage, damage_list

move = "Aerial Ace"
pkm1 = Pokemon("Chikorita", 50, [move], None, None, [4,252,0,0,0,252], [31,31,31,31,31,31], "adamant", "fire")
pkm2 = Pokemon("Metapod", 50, [move], None, None, [252,0,252,0,4,0], [31,31,31,31,31,31], "bold", "fire")

#check stats calc
print("{}, lv ".format(pkm1.specie), pkm1.lv)
print("with spread: ", pkm1.EVs, pkm1.nature)
print("has the following stats: ", pkm1.stats)
print("{}, lv ".format(pkm2.specie), pkm2.lv)
print("with spread: ", pkm2.EVs, pkm2.nature)
print("has the following stats: ", pkm2.stats)

#check damage calc
print("{} attacks {} using {}".format(pkm1.specie, pkm2.specie, move))
dmg = damage(pkm1, pkm2, move)
print("dmg with roll: ", dmg)
dmgmin = damage(pkm1, pkm2, move, "min")
print("dmg min: ", dmgmin)
dmgmax = damage(pkm1, pkm2, move, "max")
print("dmg max: ", dmgmax)
dmgall = damage_list(pkm1, pkm2, move)
print("dmg rolls: ", dmgall)
