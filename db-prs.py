# coding: utf-8
'''
file structure:
<id>, <name>, <age>

]$ cat file.txt
1 Anna 20
2 Dima 23
<...>
'''

import sys
import sqlite as db

try:
    con = db.connect(database='namedb')
    cur = c.cursor()
except Exception:
    print(u'Невозможно подключиться')
    sys.exit(1)

try:
    for line in open('file.txt', 'r').readline():
        your_id, name, age = line.split()
        cu.execute('''INSERT INTO namedb (your_id, name, age) VALUES ({},'{}',{});''', rec)
    c.commit()
except FileNotFoundError:
    print(u'Файл не найден')

