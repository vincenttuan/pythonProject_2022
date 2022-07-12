# Python 物件導向 __get__、__set__
class USD:  # 美金
    def __get__(self, instance, owner):
        money = instance.money
        return money / 30


class JPY:  # 日幣
    def __get__(self, instance, owner):
        money = instance.money
        return money / 0.22


class Exchange:
    usd = USD()
    jpy = JPY()

    def __init__(self, money):
        self.money = money


if __name__ == '__main__':
    money = 10000
    exchange = Exchange(money)
    print('TWD: %d' % money)
    print('USD: %d' % exchange.usd)  # __get__
    print('JPY: %d' % exchange.jpy)  # __get__
