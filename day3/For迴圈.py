# 迴圈: 基礎迴圈 - while  使用時機: 不確定會執行幾次
#      步進迴圈 - for in  使用時機: 已知會執行幾次
# 印出 1~10
# 1. 使用 基礎迴圈 - while
x = 1
while x <= 10:  # 當 x <= 10 的時候執行
    print(x, end=' ')  # end=' ' 表示結尾放一個空白
    x = x + 1
print()
# 2. 使用 步進迴圈 - for in
# range(n, m) 範圍 n <= x < m
for x in range(1, 11):  # 特別注意: 10 + 1 = 11
    print(x, end=' ')


