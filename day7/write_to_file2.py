# 將 dict 的資料寫入到檔案
salary = [
    {'name': 'John', 'salary': 45000},
    {'name': 'Mary', 'salary': 55000},
    {'name': 'Tom', 'salary': 38000},
    {'name': 'Helen', 'salary': 65000},
    {'name': 'Boss', 'salary': 150000},
]
file = open('salary.txt', 'w', encoding='UTF-8')
for sal in salary:
    file.write(sal.get('name') + "," + str(sal.get('salary')) + "\n")
file.close()
print('資料寫入完畢')
