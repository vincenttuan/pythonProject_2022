# 猜數字遊戲
# 答案 -> 電腦隨機產生一個數字(1~9)
# 若使用者猜的數字比答案大 -> 顯示：再小一點
# 若使用者猜的數字比答案小 -> 顯示：再大一點
# 若使用者猜的數字等於答案 -> 顯示：賓果
import random
ans = random.randint(1, 9)
while True:
    user_guess = int(input('1~9 請猜一個數字: '))
    if user_guess > ans:
        print('再小一點')
        continue
    elif user_guess < ans:
        print('再大一點')
        continue
    else:
        print('賓果')
        break
