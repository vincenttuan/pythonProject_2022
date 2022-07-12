# Python 物件導向-物件比較
# > (__gt__)
# >= (__ge__)
# < (__lt__)
# <= (__le__)
# == (__eq__)

class Drink:
    def __init__(self, name, amount, total_price):
        self.name = name
        self.amount = amount
        self.total_price = total_price

    def __gt__(self, other):
        return (self.total_price/self.amount) > (other.total_price/other.amount)

    def __lt__(self, other):
        return (self.total_price/self.amount) < (other.total_price/other.amount)


if __name__ == '__main__':
    milk = Drink('牛奶', 3, 80)
    coffee = Drink('咖啡', 2, 110)
    print(80/3, 110/2)
    print(milk > coffee)
    print(milk < coffee)
    # 哪一個飲料單價較便宜
    name = milk.name if milk < coffee else coffee.name
    print('要便宜的飲料是: %s' % name)
