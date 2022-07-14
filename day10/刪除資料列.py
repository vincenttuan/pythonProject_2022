# 刪除資料列
import sqlite3


def delete_record(id):
    sql = 'delete from employee where id=%d' % id
    print(sql)


if __name__ == '__main__':
    id = int(input('請輸入要刪除的 id 編號: '))
    delete_record(id)

