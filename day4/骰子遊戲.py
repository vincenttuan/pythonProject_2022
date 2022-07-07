# 骰子遊戲
# 本金 balance 100
# 下注 bet 金額不可超過本金
# 若本金 = 0 直接離開遊戲
# 玩家可以選擇 (2: 比大, 1: 比小, 0: 離開遊戲)
# 玩家最多可以玩 5 個回合 round_value (使用 for-in 迴圈)
balance = 100  # 本金
bet = 0  # 下注金額
round_value = 5  # 回合
dice = [0, 0, 0]  # 骰子
for i in range(1, round_value+1):
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






