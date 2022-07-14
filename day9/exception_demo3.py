apple = 10  # 蘋果數量
nums = [2, 0, 5]  # 人數
#       0  1  2   # 位置


def get_index():  # 取得 index 的函式
    # 利用錯誤處理驗證
    try:
        idx = int(input('請輸入人數位置 0=2, 1=0, 2=5: '))
    except ValueError as ve:
        print('輸入了非數字資料:', ve)
        return False, None

    # 利用程式邏輯驗證
    if idx < 0 or idx > len(nums) - 1:
        print('超過 nums 位置(index)可選範圍')
        return False, None

    if nums[idx] == 0:
        print('分母不可為0')
        return False, None

    return True, idx


if __name__ == '__main__':
    print('蘋果有 %d 個' % apple)
    success, idx = get_index()
    if success:
        # 正式進入計算程序
        print('有 %d 人分' % nums[idx])
        avg = apple / nums[idx]
        print('每個人可以得到 %d 個蘋果' % avg)
    else:
        print('資料有誤！程式停止~')
