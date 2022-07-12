# 行政院農委會食用米抽檢不合格商品資料
# 網址: https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx
import requests
import json


def load_json_data():  # 將資料載入到 json 物件中
    url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
    json_data = json.loads(requests.get(url).text)
    return json_data


def data_analyzing(name):  # 根據 name(品名) 的內容進行搜尋
    json_data = load_json_data()
    for data in json_data:
        if name in data['品名']:  # 關鍵字比對
            print('品名: %s 不合格原因: %s' % (data['品名'], data['不合格原因']))


if __name__ == '__main__':
    data_analyzing('池上')
