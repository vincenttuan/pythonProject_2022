# 讀檔(r: read) -> 進行分析計算
# 覆寫/寫入(w: write)
# 新增/寫入(a: append)
file = open('salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
print(type(rows), rows)
# 進行資料整理
# 將 list<str> : ['John,45000\n', 'Mary,55000\n', 'Tom,38000\n', 'Helen,65000\n', 'Boss,150000\n']
# 變 list<dict>: [{'name': 'John', 'salary': 45000}, {'name': 'Mary', 'salary': 55000}, ...]
employees = []  # 建立一個空的數組(容器)
for row in rows:
    row = row.strip('\n')  # 去除 \n
    array = row.split(",")  # 透過 ',' 來切分資料
    name = array[0]  # 姓名
    salary = int(array[1])  # 薪資
    data = {'name': name, 'salary': salary}  # dict/json 的格式
    employees.append(data)  # 將 data 放入到 employees 中

print(type(employees), employees)

# 進行資料分析
# 計算出薪資的總和與平均
total = 0
for emp in employees:
    total += emp.get('salary')  # total = total + emp.get('salary')
avg = total / len(employees)
print('薪資總合: %d 薪資平均: %.1f' % (total, avg))
print('薪資總合: %s 薪資平均: %s' % (format(total, ','), format(float('%.1f' % avg), ',')))




