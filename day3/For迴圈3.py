# 九九乘法表
# 1*1=1 1*2=2 1*3=3 ... 1*9=9
# 2*1=2 2*2=4 2*3=6 ... 2*9=18
# ...
# 9*1=9 9*2=18 9*3=27 ... 9*9=81
# 雙層迴圈
min_value, max_value = 1, 10
for x in range(min_value, max_value):
    for y in range(min_value, max_value):
        print("%2d*%2d=%3d" % (x, y, (x * y)), end=' ')
    print()





