# 高階函式
# 將函式作為參數

def add(x):  # 一般函式
    return x + 1


def sub(x):  # 一般函式
    return x - 1


def computer(func, x):  # 高階函式
    result_value = func(x)
    return result_value


if __name__ == '__main__':
    result = computer(add, 10)
    print(result)

    # result = add(10)
    # print(result)
    # result = sub(10)
    # print(result)
