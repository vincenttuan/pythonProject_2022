# Python 物件導向
class Person:  # 類別，物件的結構(藍圖)
    name = ''  # 姓名。物件屬性/變數/欄位/資產
    sex = ''   # 姓別。物件屬性/變數/欄位/資產
    age = 0    # 年齡。物件屬性/變數/欄位/資產


if __name__ == '__main__':
    p1 = Person()  # 建立一個 Person 物件
    p2 = Person()  # 建立一個 Person 物件

    p1.name = 'Vincent'  # 設定物件屬性資料
    p1.sex = '男'
    p1.age = 18

    p2.name = 'Anita'
    p2.sex = '女'
    p2.age = 19

    print(p1.name, p1.sex, p1.age)
    print(p2.name, p2.sex, p2.age)

