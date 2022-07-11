# 自訂方法內調用其他自訂方法
import def_demo3 as calc


def getAreaAndVolume(r):
    area = calc.getArea(r)
    volume = calc.getVolume(r)
    return area, volume


if __name__ == '__main__':
    r = 10
    area_value, volume_value = getAreaAndVolume(r)
    print('半徑: %d 圓面積: %.1f' % (r, area_value))
    print('半徑: %d 球體積: %.1f' % (r, volume_value))