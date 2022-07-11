# 自訂函示（帶參數 + 有回傳值）
# -> int : 表示方法的回傳值別是 int(整數)
# -> int : 不一定要撰寫
def add(x, y) -> int:
    result = x + y
    return result


if __name__ == '__main__':
    x = add(10, 20)
    print('x =', x)
