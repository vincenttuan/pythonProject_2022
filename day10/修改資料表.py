# 修改資料表
import sqlite3


# 根據 id 找到該筆資料，並且修改 salary 內容
def update_salary(id, salary):
    sql = 'update employee set salary=%d where id=%d' % (salary, id)
    print(sql)
    # 進行資料表修改程序
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    print('修改筆數:', cursor.rowcount)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    id = int(input('請輸入 id: '))
    salary = int(input('請輸入薪資: '))
    update_salary(id, salary)

