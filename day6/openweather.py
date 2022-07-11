# OpenWeather 爬蟲
# 目的：取得台北市最新天氣資料
import requests
import json
import ssl
import datetime
# 不用驗證 SSL
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s'
city_name = 'taipei'
country_code = 'tw'
key = '2295875238b05edcf8c6e39db1ffc3d2'  # 請不要使用此 key, 要用自己申請的
# 組合 url
url = url % (city_name, country_code, key)
print(url)
# 爬取網頁資料
resp = requests.get(url)
print(resp.status_code)  # 回應碼：200 表示 OK
print(type(resp.text), resp.text)  # 回應網頁文字內容
# 將網頁文字轉換成 json 物件，如此才可以處理與分析
ow = json.loads(resp.text)
print(type(ow), ow)
# 溫度/體感溫度/濕度
temp = ow['main']['temp']  # 絕對溫度
temp = temp - 273.15
print('溫度: %.2f°C' % temp)
feels_like = ow['main']['feels_like']
feels_like = feels_like - 273.15
print('體感溫度: %.2f°C' % feels_like)
humidity = ow['main']['humidity']
print('濕度: %d%%' % humidity)
# 天氣說明
description = ow['weather'][0]['description']
print('天氣說明: %s' % description)
# 時間
dt = ow['dt']
dt = datetime.datetime.fromtimestamp(dt).strftime('%Y-%m-%d %H:%M:%S')
print('時間: %s' % dt)



