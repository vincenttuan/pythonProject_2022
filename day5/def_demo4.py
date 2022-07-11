# 使用自訂函示
# 使用在 def_demo3.py 中已經實作好的自訂函示
import def_demo3

if __name__ == '__main__':
    r = 10
    area_value = def_demo3.getArea(r)
    volume_value = def_demo3.getVolume(r)
    print('半徑: %d 圓面積: %.1f' % (r, area_value))
    print('半徑: %d 球體積: %.1f' % (r, volume_value))
