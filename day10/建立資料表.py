# 建立一個員工 employee 資料表
import sqlite3  # python 3 之後內建支援的小型資料庫
# 建立資料表 sql 語句
sql = '''
    create table if not exists employee(
        id integer not null primary key autoincrement,
        name text not null,
        salary integer
    )
'''
sql = sql.strip()  # 去除文字的前後空白
print(sql)
# 1. 開啟資料庫連線
# 若 demo.db 資料庫不存在，會自動建立
conn = sqlite3.connect('demo.db')
# 2. 得到 cursor 指標，用來操作資料表/庫
cursor = conn.cursor()
# 3. 執行 sql 指令
cursor.execute(sql)
# 4. 任務提交
conn.commit()
# 5. 關閉資料庫連線
conn.close()
print('資料表建立完成')
