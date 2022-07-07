# 猜數字對戰版
# 答案 -> 電腦隨機產生一個數字(1~9)
# 若玩家/PC猜的數字比答案大 -> 顯示：再小一點
# 若玩家/PC猜的數字比答案小 -> 顯示：再大一點
# 若玩家/PC猜的數字等於答案 -> 顯示：賓果 (玩家/PC贏了)
import random

min_num, max_num = 1, 9
ans = random.randint(min_num, max_num)
while True:
    # 玩家 玩
    player_guess = input('玩家輸入 %d~%d 數字: ' % (min_num, max_num))
    # 判斷玩家所輸入資料是否字串內容都是數字 ?
    if player_guess.isdigit():
        player_guess = int(player_guess)  # 將字串轉成數字
    else:
        print('輸入數字')
        continue
    # 判斷玩家所輸入資料是否在合法的區間之內
    if player_guess < min_num or player_guess > max_num:
        print('數字範圍錯誤，請重新輸入！')
        continue
    if player_guess > ans:
        print('玩家:再小一點')
        max_num = player_guess - 1
    elif player_guess < ans:
        print('玩家:再大一點')
        min_num = player_guess + 1
    else:
        print('賓果 (玩家贏了)')
        break
    '''
    情境：
    ans = 6
    player_guess = 8
    玩家猜得比答案大
    PC 猜的範圍就是 1~7
    
    player_guess = 3
    玩家猜得比答案小
    PC 猜的範圍就是 4~9
    '''
    # PC 玩
    pc_guess = random.randint(min_num, max_num)
    print('PC輸入 %d~%d 數字: %d' % (min_num, max_num, pc_guess))
    if pc_guess > ans:
        print('PC:再小一點')
        max_num = pc_guess - 1
    elif pc_guess < ans:
        print('PC:再大一點')
        min_num = pc_guess + 1
    else:
        print('賓果 (PC贏了)')
        break


