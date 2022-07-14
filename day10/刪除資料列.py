# 刪除資料列
import sqlite3


def delete_record(id):
    sql = 'delete from employee where id=%d' % id
    print(sql)
    # 進行資料表刪除程序
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    print('刪除筆數:', cursor.rowcount)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    id = int(input('請輸入要刪除的 id 編號: '))
    delete_record(id)

