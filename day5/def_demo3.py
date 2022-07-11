import math


# 計算圓面積
def getArea(r):
    area = math.pow(r, 2) * math.pi
    return area


# 計算球體積
def getVolume(r):
    volume = 4/3 * math.pi * math.pow(r, 3)
    return volume


if __name__ == '__main__':
    r = 10
    area_value = getArea(r)
    volume_value = getVolume(r)
    print('半徑: %d 圓面積: %.1f' % (r, area_value))
    print('半徑: %d 球體積: %.1f' % (r, volume_value))
