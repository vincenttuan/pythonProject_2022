# Python 物件導向
# __str__  # 物件以字串方式顯示, 用來幫助程式開發者觀察物件內的屬性資料變化
# __init__ # 建構式，一般用來初始設定物件屬性內容
class Person:
    def __init__(self, name, sex, age) -> None:
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self) -> str:
        return 'name: %s sex: %s age: %d' % (self.name, self.sex, self.age)


if __name__ == '__main__':
    p1 = Person('Vincent', '男', 18)
    print(p1)
