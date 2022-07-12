# Python 物件導向-封裝
class Account:
    __balance = 0  # 私有變數

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return '%s 的帳戶餘額 $%d' % (self.name, self.__balance)


if __name__ == '__main__':
    act1 = Account('John')  # 開戶
    print(act1)
