# 物件與運算子
# +(__add__)
# -(__sub__)
# *(__mul__)
# /(__div__)
# %(__mod__)
# **(__pow__)
class Number:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        self.n += other

    def __sub__(self, other):
        self.n -= other


if __name__ == '__main__':
    x = Number(10)
    x + 15
    x - 13
    print(x)
