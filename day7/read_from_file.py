# 讀檔 -> 進行分析計算
file = open('salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
print(type(rows), rows)
# 進行資料整理
# 將 list: ['John,45000\n', 'Mary,55000\n', 'Tom,38000\n', 'Helen,65000\n', 'Boss,150000\n']
# 變 dict: [{'name': 'John', 'salary': 45000}, {'name': 'Mary', 'salary': 55000}, ...]
employees = []  # 建立一個空的數組(容器)
for row in rows:
    row = row.strip('\n')  # 去除 \n
    array = row.split(",")  # 透過 ',' 來切分資料
    name = array[0]  # 姓名
    salary = int(array[1])  # 薪資
    data = {'name': name, 'salary': salary}  # dict 的格式
    employees.append(data)  # 將 data 放入到 employees 中

print(type(employees), employees)




