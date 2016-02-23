# coding: utf-8
'''
Python 3
file structure:
<id>, <name>, <age>

]$ cat file.txt
1 Anna 20
2 Dima 23
<...>
'''

import sys
import sqlite3 as db


connection = db.connect(database='test.db')
cursor = connection.cursor()

try:
    for line in iter(open('file.txt', 'r').readline, ''):
        your_id, name, age = line.split()
        cursor.execute(
        	'''INSERT INTO table1 (id, name, age) VALUES ({},'{}',{});'''
        	.format(your_id, name, age)
        	)
    connection.commit()
except FileNotFoundError:
    print(u'Файл не найден')
except db.OperationalError as db_exception:
	print(u'Не удалось вставить данные в базу:\n{}'.format(db_exception))
except Exception as unhadled_exception:
	print(u'Непредвиденная ошибка:\n{}'.format(unhadled_exception))
