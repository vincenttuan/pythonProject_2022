import random  # 隨機數
# while 迴圈控制
# while 迴圈判斷到 True 會繼續執行，反之 False 離開迴圈
while True:
    num = random.randint(1, 100)  # 1~100 的隨機數
    if num % 2 == 1:  # 奇數才要印
        print(num)
    else:
        continue  # 直接進入下一次的迴圈判斷
    if num == 99:
        break  # 停止迴圈
        print('停止迴圈')
