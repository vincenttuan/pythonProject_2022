# 透過 'a' 累計加入資料
# 透過 'w' 重新覆蓋資料
import datetime

message = input('請輸入任意資料: ')
file = open('message.txt', 'a', encoding='UTF-8')
file.write('訊息: ' + message + ' 寫入時間: ' + str(datetime.datetime.now()) + '\n')
file.close()
print('寫入完畢!')
