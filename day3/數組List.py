# Python 數組 list
# list = [1, 3, 5, 7, 5] 元素內容可以重複, 元素內容可以修改
x = [1, 3, 5, 7, 5]
# 數組: [1, 3, 5, 7, 5]
# 位置:  0  1  2  3  4
print(x, type(x), len(x))
# 增加元素
x.append(4)
print(x)
print('5出現的次數:', x.count(5))
try:
    print('7有無在該數組中:', x.index(7))
    print('9有無在該數組中:', x.index(9))
except ValueError as ve:
    print(ve)
# 移除指定元素
x.remove(5)
print(x)
# 反轉
x.reverse()
print(x)
# 最大/最小元素內容
print('max:', max(x), ' min:', min(x))
