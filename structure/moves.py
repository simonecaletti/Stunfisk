#!/bin/python3

import sqlite3

path = "./database/moves/"
mvdb = "moves.db"

def get_mv_pwr(move):
    db = sqlite3.connect(path + mvdb)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM move WHERE name = '{}'".format(move))
    table = cursor.fetchall()
    pwr = table[0][1]

    return pwr

def get_mv_type(move):
    db = sqlite3.connect(path + mvdb)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM move WHERE name = '{}'".format(move))
    table = cursor.fetchall()
    tp = table[0][2]

    return tp

def get_mv_category(move):
    db = sqlite3.connect(path + mvdb)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM move WHERE name = '{}'".format(move))
    table = cursor.fetchall()
    cat = table[0][3]

    return cat

def get_mv_priority(move):
    db = sqlite3.connect(path + mvdb)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM move WHERE name = '{}'".format(move))
    table = cursor.fetchall()
    prio = table[0][4]

    return prio

class Move:
    def __init__(self, name):
        self.name = name
        self.pwr = get_mv_pwr(name)
        #self.sec_eff = 
        self.type = get_mv_type(name)
        self.category = get_mv_category(name)
        self.priority = get_mv_priority(name)


