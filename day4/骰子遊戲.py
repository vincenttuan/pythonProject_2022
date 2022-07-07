# 骰子遊戲
# 本金 balance 100
# 下注 bet 金額不可超過本金
# 若本金 = 0 直接離開遊戲
# 玩家可以選擇 (2: 比大, 1: 比小, 0: 離開遊戲)
# 玩家最多可以玩 5 個回合 round_value (使用 for-in 迴圈)
import random
balance = 100  # 本金
bet = 0  # 下注金額
round_value = 5  # 回合
dice = [0, 0, 0]  # 骰子
for i in range(1, round_value+1):
    # 顯示玩家餘額
    print('玩家餘額：', balance)
    # 系統先擲骰子
    dice = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    dice_sum = sum(dice)
    # 1. 檢查本金是否 > 0
    if balance <= 0:
        print('本金不足:', balance, ' 離開遊戲!')
        break
    # 2. 輸入 2:比大, 1:比小, 0:離開
    flag = int(input('第 %d 回合 2:比大, 1:比小, 0:離開：' % i))
    if flag > 2 or flag < 0:
        print('輸入錯誤！請重新輸入')
        continue
    if flag == 0:
        print('離開遊戲!')
        break
    # 3. 下注
    bet = int(input('第 %d 回合 請下注：' % i))
    # 4. 檢查下注金額
    if bet > balance:
        print('下注金額過大:', bet, ' 本金:', balance)
        continue
    # 5. 扣抵 balance
    balance = balance - bet
    # 6. 判斷輸贏
    if flag == 2 and dice_sum > 10:  # 比大贏了
        print('玩家猜大贏了')
        balance = balance + (2*bet)
    elif flag == 1 and dice_sum <= 10:  # 比小贏了
        print('玩家猜小贏了')
        balance = balance + (2 * bet)
    else:
        print('玩家輸了')
    # 7. 開盅(揭露骰子的資訊)
    print('骰子點數：', dice, ' 總和:', dice_sum, '小' if dice_sum <= 10 else '大')

# 最後顯示玩家餘額
print('玩家餘額：', balance)
