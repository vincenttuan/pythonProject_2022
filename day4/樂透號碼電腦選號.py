import random
# 四星彩(數字可重複版)
# 0~9 任意取出 4 個數字, 數字可以重複
four_stars = []
for i in range(0, 4):
    n = random.randint(0, 9)
    print('n =', n)
    four_stars.append(n)
print(four_stars, len(four_stars))
# 四星彩(數字不可重複版)
# 0~9 任意取出 4 個數字, 數字不可以重複

