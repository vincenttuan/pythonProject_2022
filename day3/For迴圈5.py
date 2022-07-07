# for 迴圈
for i in range(1, 10):  # 1..9
    print(i, 'Java')

for i in range(1, 10, 3):  # 1, 4, 7
    print(i, 'Python')

for i in [10, 20, 30, 40, 50]:  # 走訪數組/陣列[]資料
    print(i, '數組元素')

# enumerate = 列舉
# score = [100, 90, 80]
#     i =   0   1   2
for i, score in enumerate([100, 90, 80]):
    print(i, score)
