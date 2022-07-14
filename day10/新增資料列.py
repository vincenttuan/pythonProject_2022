# 新增資料列
import sqlite3

# 將 name, salary 加入到 employee 資料表中
def insert_to_table(name, salary):
    # 新增資料列 sql
    sql = '''
        insert into employee(name, salary)
        values('%s', %d)
    '''
    sql = sql.strip() % (name, salary)
    print(sql)
    # 連線到資料庫並進行新增程序
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    print('新增筆數:', cursor.rowcount)
    print('取得最新 id 值:', cursor.lastrowid)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # John, 40000  Mary, 38000   Bob, 57000
    name = input('請輸入員工姓名: ')
    salary = int(input('請輸入員工薪資: '))
    insert_to_table(name, salary)

