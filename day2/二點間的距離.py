import math  # 匯入數學資源
# 求二點間的距離
# x1, y1 = 10, 20
# x2, y2 = 15, 45
print("圓周率:", math.pi)
x1, y1 = 10, 20
x2, y2 = 15, 45
# x1, y1, x2, y2 = 10, 20, 15, 45
dx = (x1 - x2)**2
dy = math.pow((y1 - y2), 2)  # 相當於 (y1 - y2)**2
d = math.sqrt(dx + dy)
print(d)
