from structure.moves import Move
import math
import random as rand

#weakness and resistence, tp1 is attacking
def get_type_int(tp):
    match tp:
        case "normal":
            return 0
        case "fire":
            return 1
        case "water":
            return 2
        case "electric":
            return 3
        case "grass":
            return 4
        case "ice":
            return 5
        case "fighting":
            return 6
        case "poison":
            return 7
        case "ground":
            return 8
        case "flying":
            return 9
        case "psychic":
            return 10
        case "bug":
            return 11
        case "rock":
            return 12
        case "ghost":
            return 13
        case "dragon":
            return 14
        case "dark":
            return 15
        case "steel":
            return 16
        case "fairy":
            return 17
        case _:
            return None

def type_matrix_entry(int1, int2):
    
    matr = [[1,   1,   1, 1,   1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],
            [1, 0.5, 0.5, 1,   2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],
            [1,   2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],
            [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],
            [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],
            [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],
            [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],
            [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],
            [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],
            [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],
            [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],
            [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],
            [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],
            [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],
            [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],
            [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]
            ]

    return matr[int1][int2]

def get_type_interaction(type1, type2):
    return type_matrix_entry(get_type_int(type1), get_type_int(type2))

#pkm1 is attacking, not complete
def base_damage(pkm1, pkm2, move):
   
    #step1
    dmg = math.floor(2*pkm1.lv/5 + 2)
    
    #check if move in moveset
    if move not in pkm1.moves: return 

    #step2, get move info
    mv = Move(move)
    if mv.category == "physical":
        dmg = math.floor(dmg*mv.pwr*pkm1.stats[1]/pkm2.stats[2])
    elif mv.category == "special":
        dmg = math.floor(dmg*mv.pwr*pkm1.stats[3]/pkm2.stats[4])
    else:
        print("No move category, maybe status move")
        return
    
    #step3
    dmg = math.floor(dmg/50) + 2 

    return dmg

def dmg_roll(mode="random"):
    match mode:
        case "max":
            return 1
        case "min":
            return 0.85
        case _:
            return rand.randrange(85, 101, 1)/100

def all_dmg_roll():
    return [x/100 for x in range(85, 101, 1)]

def STAB(mv, pkm):
    if mv.type == pkm.typing:
        if pkm.ability == "adaptability":
            return 2
        else:
            return 1.5
    else:
        return 1

def type_int_fact(mv, pkm):
    fact = get_type_interaction(mv.type, pkm.typing[0])
    if pkm.typing[1] is not None:
        fact = fact*get_type_interaction(mv.type, pkm.typing[1])
    return fact

def damage(pkm1, pkm2, move, roll="random"):
    
    mv = Move(move) 
    dmg = base_damage(pkm1, pkm2, move)
   
    #add roll
    dmg = dmg*dmg_roll(roll)
    #add STAB
    dmg = dmg*STAB(mv, pkm1)
    #add type effectiveness
    dmg = dmg*type_int_fact(mv, pkm2)

    return math.floor(dmg)

def damage_list(pkm1, pkm2, move):
    
    mv = Move(move)
    dmg = base_damage(pkm1, pkm2, move)

    #get all roll
    dmg_list = [math.floor(dmg*r) for r in all_dmg_roll()]
    #add STAB
    dmg_list = [dmg*STAB(mv, pkm1) for dmg in dmg_list]
    #add type effectiveness
    dmg_list = [dmg*type_int_fact(mv, pkm2) for dmg in dmg_list]

    return dmg_list
