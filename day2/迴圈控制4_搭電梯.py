# 搭電梯
# 幸福大廈 1~7 層
# 指定要去的樓層 1-7 輸入: 0 離開電梯
import time
min_floor, max_floor = 1, 7
cur_floor = 1  # 目前電梯所在樓層
tar_floor = 0  # 要到達的樓層
while True:
    tar_floor = int(input('電梯目前停在 %d 樓, 請輸入要到達的樓層 %d - %d (0:離開電梯): ' % (cur_floor, min_floor, max_floor)))
    if tar_floor == 0:
        break
    if tar_floor < min_floor or tar_floor > max_floor:  # 判斷是否超過樓層範圍?
        print('本大廈無此樓層！')
        continue
    if tar_floor == cur_floor:
        print('本電梯已經到了')
        continue
    # 電梯上樓
    if tar_floor > cur_floor:
        print('電梯上樓')
        # 電梯運行
        while True:
            time.sleep(1)  # 延遲 1 秒鐘，模擬電梯的運作
            cur_floor = cur_floor + 1
            print(cur_floor)
            if cur_floor == tar_floor:
                print('電梯到了')
                break
    # 電梯下樓
    elif tar_floor < cur_floor:
        print('電梯下樓')
        while True:
            time.sleep(1)  # 延遲 1 秒鐘，模擬電梯的運作
            cur_floor = cur_floor - 1
            print(cur_floor)
            if cur_floor == tar_floor:
                print('電梯到了')
                break
