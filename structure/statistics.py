import math

def get_hp(base, lv, ev, iv):

    hp = 2*base + iv + math.floor(ev/4)
    hp = hp*lv/100
    hp = math.floor(hp) + lv + 10

    return hp

def get_stat(base, lv, ev, iv, nat):

    stat = 2*base + iv + math.floor(ev/4)
    stat = stat*lv/100
    stat = math.floor(stat) + 5
    stat = math.floor(stat*nat)

    return stat

def get_nature(nature):
    match nature:
        case "serious":
            return [1, 1, 1, 1, 1]
        case "adamant":
            return [1.1, 1, 0.9, 1, 1]
        case "bashful":
            return [1, 1, 1, 1, 1]
        case "bold":
            return [0.9, 1.1, 1, 1, 1]
        case "brave":
            return [1.1, 1, 1, 1, 0.9]
        case "calm":
            return [0.9, 1, 1, 1.1, 1]
        case "careful":
            return [1, 1, 0.9, 1.1, 1]
        case "docile":
            return [1, 1, 1, 1, 1]
        case "gentle":
            return [1, 0.9, 1, 1.1, 1]
        case "hardy":
            return [1, 1, 1, 1, 1]
        case "hasty":
            return [1, 0.9, 1, 1, 1.1]
        case "impish":
            return [1, 1.1, 0.9, 1, 1]
        case "jolly":
            return [1, 1, 0.9, 1, 1.1]
        case "lax":
            return [1, 1.1, 1, 0.9, 1]
        case "lonely":
            return [1.1, 0.9, 1, 1, 1]
        case "mild":
            return [1, 0.9, 1.1, 1, 1]
        case "modest":
            return [0.9, 1, 1.1, 1, 1]
        case "naive":
            return [1, 1, 1, 0.9, 1.1]
        case "naughty":
            return [1.1, 1, 1, 0.9, 1]
        case "quiet":
            return [1, 1, 1.1, 1, 0.9]
        case "quirky":
            return [1, 1, 1, 1, 1]
        case "rash":
            return [1, 1, 1.1, 0.9, 1]
        case "relaxed":
            return [1, 1.1, 1, 1, 0.9]
        case "sassy":
            return [1, 1, 1, 1.1, 0.9]
        case "timid":
            return [0.9, 1, 1, 1, 1.1]
        case _:
            print("Nature does not exist")
            return None

