# 假設要定義一組運算 f(x) = x * x - x
def calc(x):
    result_value = x * x - x
    return result_value


if __name__ == '__main__':
    x = 10
    result = calc(x)
    print('x: %d result: %d' % (x, result))
    # Lambda 運算
    # func 就是一個 Lambda 的函示
    func = lambda x: x * x - x  # f(x) = x * x - x
    x = 20
    result = func(x)
    print('x: %d result: %d' % (x, result))
