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
    bad_food = []
    for data in json_data:
        if name in data['品名']:  # 關鍵字比對
            bad_food.append('品名: %s 不合格原因: %s' % (data['品名'], data['不合格原因']))
    return bad_food


def write_to_file(data, file_name):  # 將結果寫入到檔案
    file = open(file_name, 'w', encoding='UTF-8')
    for row in data:
        file.write(row + '\n')
    file.close()


if __name__ == '__main__':
    bad_food = data_analyzing('池上')
    print(bad_food)
    write_to_file(bad_food, 'bad_food.txt')
    print('寫檔完畢')
