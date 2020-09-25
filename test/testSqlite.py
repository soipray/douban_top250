# -*- codeing = utf8 -*-
# @Time 2020/9/14 13:31
# @Author : xxx
# @File : testSqlite.py
# @Software: PyCharm

import sqlite3
conn = sqlite3.connect("test.db")
print("Open database successfully")

c = conn.cursor()

sql = '''
    create table if not exists company (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name text not null,
        age int not null,
        address char(50),
        salary real
    );
'''
c.execute(sql)
conn.commit()

#插入数据
sql = '''
insert into company (address,age,name,salary)
values ("address1",10,"name1",800)
;
'''
c.execute(sql)
conn.commit()
print("insert success")

sql = "select id ,name ,address ,salary from company where 1 = 1 "
cursor = c.execute(sql)
for row in cursor:
    print(row)
print("query ok")

conn.close()
print("close database")

