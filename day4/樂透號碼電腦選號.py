import random
# 四星彩(數字可重複版)
# 0~9 任意取出 4 個數字, 數字可以重複
four_stars = []
for i in range(0, 4):
    n = random.randint(0, 9)
    print('n =', n)
    four_stars.append(n)
print(four_stars, len(four_stars))

print('----------------')
# 四星彩(數字不可重複版)
# 0~9 任意取出 4 個數字, 數字不可以重複
four_stars = []
while len(four_stars) < 4:
    n = random.randint(0, 9)
    print('n =', n)
    try:
        # n 是否在 four_stars 中
        # 若 n 沒有在 four_stars 中則會拋出例外
        four_stars.index(n)
    except ValueError as ve:
        four_stars.append(n)

print(four_stars, len(four_stars))


