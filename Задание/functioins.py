import sqlite3
import pprint
import random
import pathlib


def inf():
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    a = 0
    b = 1
    while a<b:
        a = random.randint(250, 300)
        b = random.randint(270, 300)
    cur.execute(data[7])
    fet = cur.fetchall()[-1:]
    c = fet[0][0]
    d = fet[0][1]
    cur.execute(data[6], (c, a, b, d))
    con.commit()
    return 1


def selecting(nom=0):
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    cur.execute(data[5], (nom,))
    pprint.pprint(cur.fetchall())
    return 1


def table():
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    print("\t\tТаблица рейсов")
    cur.execute(data[3])
    pprint.pprint(cur.fetchall())
    print("\t\tТаблица информации о самолёте")
    cur.execute(data[4])
    pprint.pprint(cur.fetchall())
    return 1


def adding(stay=0, number=0, value=0):
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cur= con.cursor()
    cur.execute(data[2],(stay, number, value))
    con.commit()
    return 1


def sql_connection():
    file = 'mydatebase.db'
    con = sqlite3.connect(file)
    return 1
        

def sql_table():
    con = sqlite3.connect('mydatebase.db')
    file = pathlib.Path.cwd()/'inf.sql'
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().split(';')
    cursor_obj = con.cursor()
    cursor_obj.execute(data[0])
    cursor_obj.execute(data[1])
    con.commit()
    return 1
