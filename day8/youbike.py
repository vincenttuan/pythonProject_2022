# Youbike json
# 網址: https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
import json
import requests
from math import radians, cos, sin, asin, sqrt

class Youbike:
    def __init__(self, sno, sna, sbi, bemp, tot, lat, lng):
        self.sno = sno
        self.sna = sna
        self.sbi = sbi
        self.bemp = bemp
        self.tot = tot
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return '站點: %s 站名: %s 可借: %d 可還 %d 全部: %d 緯度: %f 經度: %f' % \
               (self.sno, self.sna, self.sbi, self.bemp, self.tot, self.lat, self.lng)


def import_data_to_youbike():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    data_json = json.loads(requests.get(url).text)
    youbikes = []
    for data in data_json:
        youbike = Youbike(data['sno'], data['sna'], data['sbi'], data['bemp'], data['tot'], data['lat'], data['lng'])
        youbikes.append(youbike)
    return youbikes


# 透過經緯度計算距離的方法
def haversine(lon1, lat1, lon2, lat2) -> int: # 經度1，緯度1，經度2，緯度2）
    # 轉弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # 半正矢 haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半徑(公里)
    return c * r * 1000 # 單位公尺


if __name__ == '__main__':
    # 巨匠東區認證中心經緯度
    lat, lng = 25.04195, 121.55045
    youbikes = import_data_to_youbike()
    print('筆數: %d' % len(youbikes))
    for youbike in youbikes:
        d = haversine(lng, lat, youbike.lng, youbike.lat)
        if d < 300:  # 距離巨匠東區認證中心 300 公尺內的站點資訊
            print(d, youbike)
