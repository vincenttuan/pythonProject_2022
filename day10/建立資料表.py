# 建立一個員工 employee 資料表
import sqlite3  # python 3 之後內建支援的小型資料庫
sql = '''
    create table if not exists employee(
        id integer not null primary key autoincrement,
        name text not null,
        salary integer
    )
'''
sql = sql.strip()  # 去除文字的前後空白
print(sql)
