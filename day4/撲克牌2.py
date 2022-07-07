import random
# 撲克牌
poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
#         0   1  2  3  4  5  6  7  8   9   10   11   12
print(poker, len(poker))
# for-in + 隨機洗牌
for i in range(0, 100):
    x = random.randint(0, len(poker)-1)
    y = random.randint(0, len(poker)-1)
    poker[x], poker[y] = poker[y], poker[x]
print(poker)

# 透過 random.shuffle() 來隨機洗牌
random.shuffle(poker)
print(poker)
