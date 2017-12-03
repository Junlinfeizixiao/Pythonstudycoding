import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# #cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id,name) values (\'1\',\'Tom\')')
# cursor.execute('insert into user (id,name) values (\'2\',\'Anna\')')
# cursor.execute('insert into user (id,name) values (\'3\',\'Jerry\')')
# print(cursor.rowcount)
# cursor.close()
# conn.commit()
# conn.close()

#查询
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()

# cursor.execute('select * from user')
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()
# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    #' 返回指定分数区间的名字，按分数从低到高排序 '
	try:
		conn = sqlite3.connect(db_file)
		cursor = conn.cursor()
		cursor.execute('select name from user where score > ? and score <= ? order by score asc',(low,high))
		values = cursor.fetchall()
	finally:
		cursor.close()
		conn.close()
	return list(map(lambda x: x[0], values))
# 测试:

print(get_score_in(80, 95))
print(get_score_in(60, 80))
print(get_score_in(60,100))


print('Pass')