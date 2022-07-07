# 變數的應用
# r 半徑 pi 圓周率
r = 15  # 半徑(cm)
pi = 3.1415926  # 圓周率
# 計算圓面積 area
area = r * r * pi
print(area)
area = r**2 * pi
print(area)
# 計算球體積 volume
# 球體積公式: 4/3 * 圓周率 * 半徑的3次方
volume = 4/3 * pi * r**3
print(volume)
print("%.1f" % volume)
print("球體積:%.1f" % volume)
# %d 放一個整數, %f 放一個浮點數, %s 放一個字串
print("半徑:%d 球體積:%.1f" % (r, volume))
