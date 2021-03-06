# dict 字典格式 (key-value)
emp1 = {'name': 'John', 'salary': 55000}
emp2 = {'name': 'Mary', 'salary': 78000}
emp3 = {'name': 'Bob', 'salary': 61000}
# 將 emp1, emp2, emp3 放入 employees 數組[]中
employees = [emp1, emp2, emp3]
print(employees)
# 將每一個員工逐一列出 姓名與薪資
for emp in employees:
    print('姓名: %s 薪資: %d' % (emp['name'], emp['salary']))
    # 將薪資加上,(千分號)
    print('姓名: %s 薪資: %s' % (emp['name'], format(emp['salary'], ',')))

# 請計算出員工總薪資與平均薪資各為何？
total = 0
for emp in employees:
    total = total + emp['salary']
print('總薪資：', total)
print('總薪資：%s' % format(total, ','))  # 加上千分號
avg = total / len(employees)
print('平均薪資：', avg)
print('平均薪資：', int(avg))  # 取整數
print('平均薪資：%s' % format(int(avg), ','))  # 加上千分號
