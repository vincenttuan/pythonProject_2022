# Youbike json
# 網址: https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
import json
import requests


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
