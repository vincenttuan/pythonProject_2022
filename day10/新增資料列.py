# 新增資料列
import sqlite3

# 將 name, salary 加入到 employee 資料表中
def insert_to_table(name, salary):
    # 新增資料列 sql
    sql = '''
        insert into employee(name, salary)
        value('%s', %d)
    '''
    sql = sql.strip() % (name, salary)
    print(sql)


if __name__ == '__main__':
    name = input('請輸入員工姓名: ')
    salary = int(input('請輸入員工薪資: '))
    insert_to_table(name, salary)

