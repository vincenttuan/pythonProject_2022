# Python 物件導向
# __str__  # 物件以字串方式顯示, 用來幫助程式開發者觀察物件內的屬性資料變化
class Person:
    name = ''
    sex = ''
    age = 0

    def __str__(self) -> str:
        return 'name: %s sex: %s age: %d' % (self.name, self.sex, self.age)


if __name__ == '__main__':
    p1 = Person()
    p1.name = 'Vincent'
    p1.sex = '男'
    p1.age = 18
    print(p1)  # 會自動呼叫 Person 中的 __str__(self) 方法
