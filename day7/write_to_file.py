#  將資料寫入到檔案
file = open('sample.txt', 'w', encoding='UTF-8')
file.write('Hello World\n')
file.close()
print('寫入資料完畢')
