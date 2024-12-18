#!/bin/python3

from structure.statistics import get_hp, get_stat, get_nature
import sqlite3
import os
import math

path = "./database/pokedex/"
pkmdb = ["kanto.db", "johto.db"]

def fetch_pkm(pokemon):
    for d in pkmdb:
        db = sqlite3.connect(path + d)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pokemon WHERE specie = '{}';".format(pokemon))
        table = cursor.fetchall()
        if table: #empty list counts as False statement
            return table[0]
    if not table:
        print("Pokemon not found in databases.")
        return None

def get_typing(pokemon):
    table = fetch_pkm(pokemon)
    typing = []
    typing.append(table[2])
    typing.append(table[3])

    return typing

def get_base_stats(pokemon):
    table = fetch_pkm(pokemon)
    base = []
    for i in range(7, 13, 1):
        base.append(table[i])

    return base

def get_stats(pokemon, lv, EVs, IVs, nature):
    
    stats = []
    base = get_base_stats(pokemon)

    #calculation for hp only
    hp = get_hp(base[0], lv, EVs[0], IVs[0])
    stats.append(hp)

    #get nature
    nat = get_nature(nature)

    #calculation for the other stats
    for i in range(1,6):
        s = get_stat(base[i], lv, EVs[i], IVs[i], nat[i-1])
        stats.append(s)

    return stats

def get_statsmod_fact(statmod):
    num = 2
    den = 2

    if statmod >= 0:
        num += statmod
    else:
        den += -1*statmod
    
    fact = num/den

    return fact

class Pokemon:
    def __init__(self, specie, lv,  moves, item, ability, EVs, IVs, nature, teratype, status="healty", statsmodifier=[0,0,0,0,0], critmodifier=0, accmodifier=[0,0]):
        self.specie = specie
        self.lv = lv
        self.typing = get_typing(self.specie)
        #self.movepool = list of all the legal moves?
        self.moves = moves
        self.item = item
        self.ability = ability
        self.EVs = EVs
        self.IVs = IVs
        self.teratype = teratype
        self.status = status
        self.nature = nature
        self.stats = get_stats(self.specie, self.lv, self.EVs, self.IVs, self.nature)
        self.currentHP = self.stats[0]
        self.statsmodifier = statsmodifier
        self.critmod = critmodifier
        self.accmod = accmodifier
        self.statsmod = self.apply_statsmodifier()

    def update_hp(self, new_hp):
        self.currentHP = new_hp
        return None

    def apply_statsmodifier(self):
        newstats = [self.stats[0]]
        for stat, mod in zip(self.stats[1:], self.statsmodifier):
            newstats.append(math.floor(stat*get_statsmod_fact(mod)))
        return newstats

