# Python 物件導向
# __私有變數
import math


class User:
    height = 0
    weight = 0
    __bmi = 0.0  # __私有變數

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.__bmi = weight / math.pow(height/100, 2)

    def __str__(self):
        return 'height: %d weight: %d bmi: %.1f' % (self.height, self.weight, self.__bmi)


if __name__ == '__main__':
    user1 = User(170, 60)
    user1.__bmi = 0  # 無法改變物件私有變數
    print(user1)

