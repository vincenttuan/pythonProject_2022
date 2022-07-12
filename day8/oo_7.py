# Python 物件導向-繼承
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return 'name: %s age: %d sex: %s' % (self.name, self.age, self.sex)

class Student(Person):
    def __init__(self, name, age, sex, number, grade):
        super().__init__(name, age, sex)
        self.number = number
        self.grade = grade

    def __str__(self):
        return super().__str__() + " number: %d grage: %s" % (self.number, self.grade)

if __name__ == '__main__':
    student = Student('John', 18, '男', 12, '大一')
    print(student)


