# f(m, n): 取最大值
def max_1(m, n):
    return m if m > n else n


if __name__ == '__main__':
    print(max_1(10, 20))
    print(max_1(20, 20))
    # 建立 Lambda 函式
    max_2 = lambda m, n: m if m > n else n
    print(max_2(20, 30))
    print(max_2(30, 30))
