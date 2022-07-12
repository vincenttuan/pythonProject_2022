# Python 物件導向-封裝
class Account:
    __balance = 0  # 私有變數

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return '%s 的帳戶餘額 $%d' % (self.name, self.__balance)

    def deposit(self, amount):  # 存款
        if amount > 0:
            self.__balance += amount  # self.__balance = self.__balance + amount
            return True, '存款成功'
        else:
            return False, '存款失敗。存款金額錯誤: $%d' % amount


if __name__ == '__main__':
    act1 = Account('John')  # 開戶
    success, msg = act1.deposit(1000)
    print(success, msg)
    print(act1)
