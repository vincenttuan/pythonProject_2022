# 查詢資料列
import sqlite3


def select_from_table():
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    sql = 'select id, name, salary from employee'
    cursor.execute(sql)
    rows = cursor.fetchall()  # 得到所有紀錄(根據 sql 語句)
    for row in rows:
        print(row[0], row[1], row[2])
    conn.close()


if __name__ == '__main__':
    select_from_table()
