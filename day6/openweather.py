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
print(resp.text)  # 回應網頁文字內容






