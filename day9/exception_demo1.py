apple = 10  # 蘋果數量
nums = [2, 0, 5]  # 人數
#       0  1  2   # 位置
print('蘋果有 %d 個' % apple)
try:
    idx = int(input('請輸入人數位置 0=2, 1=0, 2=5: '))
    print('有 %d 人分' % nums[idx])
    avg = apple / nums[idx]
except ValueError as ve:
    print('輸入了非數字資料:', ve)
except IndexError as ie:
    print('超過 nums 位置(index)可選範圍:', ie)
except ZeroDivisionError as zde:
    print('分母為0導致的錯誤:', zde)
else:
    print('每個人可以得到 %d 個蘋果' % avg)

# ValueError 輸入非數字資料
# IndexError 超過 nums 位置(index)可選範圍
# ZeroDivisionError 分母為0導致的錯誤

