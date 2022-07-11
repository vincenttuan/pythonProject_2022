# Lambda 與 def 函式混用
def hello() -> None:
    print('Hello')


def add(x, y) -> int:
    return x + y


if __name__ == '__main__':
    func_hello = lambda: hello()
    func_hello()
    func_add = lambda x, y: add(x, y)
    result = func_add(10, 20)
    print(result)

    (lambda: hello())()
    result = (lambda x, y: add(x, y))(10, 20)
    print(result)
