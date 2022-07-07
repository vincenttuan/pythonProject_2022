# 骰子遊戲
# 有 3 顆骰子
import random
dice = [0, 0, 0]
# dice[0] = random.randint(1, 6)
# dice[1] = random.randint(1, 6)
# dice[2] = random.randint(1, 6)
for i, d in enumerate(dice):
    print(d, end=' -> ')
    dice[i] = random.randint(1, 6)
    print(dice[i])
print(dice, '總和:', sum(dice))
# 顯示大小
# 小: 03、04、05、06、07、08、09、10
# 大: 11、12、13、14、15、16、17、18
# 請顯示此次骰子總和是大還是小
dice_sum = sum(dice)
if dice_sum <= 10:
    print('小')
else:
    print('大')
# ------------------------
print('小' if dice_sum <= 10 else '大')
