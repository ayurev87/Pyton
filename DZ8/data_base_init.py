import sqlite3


d_base = sqlite3.connect("personal.db")

curs = d_base.cursor()

title_list = ['имя', 'фамилия', 'должность', 'заработная плата', 'премия']
title_list_en = ['first_name', 'family', 'position,' 'salary', 'bonus']

curs.execute('''CREATE TABLE IF NOT EXISTS personal(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    family TEXT,
    position TEXT,
    salary INT,
    bonus INT
    )''')