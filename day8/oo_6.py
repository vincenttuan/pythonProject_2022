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
            return True, '存款成功。存款金額 $%d' % amount
        else:
            return False, '存款失敗。存款金額錯誤: $%d' % amount

    def withdrawal(self, amount):   # 提款
        if amount <= 0:
            return False, '提款失敗。提款金額錯誤: $%d' % amount

        if self.__balance >= amount:
            self.__balance -= amount  # self.__balance = self.__balance - amount
            return True, '提款成功。提款金額 $%d' % amount
        else:
            return False, '提款失敗。提款金額過大 $%d' % amount

    def transfer(self, act, amount):
        if amount <= 0:
            return False, '轉帳失敗。轉帳金額錯誤: $%d' % amount

        if self.__balance >= amount:
            # 進行轉帳程序
            self.withdrawal(amount)  # 轉帳方進行提款
            act.deposit(amount)  # 接收方進行存款
            return True, '轉帳成功。轉帳金額 $%d' % amount
        else:
            return True, '轉帳失敗。轉帳金額過大 $%d' % amount


if __name__ == '__main__':
    act1 = Account('John')  # 開戶
    act2 = Account('Mary')

    success, msg = act1.deposit(1000)  # 存款
    print(success, msg)
    print(act1)

    success, msg = act1.withdrawal(700)  # 提款
    print(success, msg)
    print(act1)

    success, msg = act1.transfer(act2, 200)  # 轉帳
    print(success, msg)
    print(act1)
    print(act2)

