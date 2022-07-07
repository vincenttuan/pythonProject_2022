# Python 數組
# list = [1, 3, 5, 7, 5] 元素內容可以重複, 元素內容可以修改
x = [1, 3, 5, 7, 5]
print(x)

# tuple = (1, 3, 5, 7, 5) 元素內容不可以修改(唯讀), 進行資料分析效率佳
y = tuple(x)  # 將 list 轉 tuple 唯讀
print(y)

# set = {1, 3, 5, 7} 內容不可重複
z = {1, 3, 5, 7, 5}  # {1, 3, 5, 7} 自動剔除重複的內容
print(z)
z = tuple(z)  # 將 set 轉 tuple 唯讀
print(z)

# dict = {'name': 'John', 'age': 18} 字典格式: key:value 的組合
person = {'name': 'John', 'age': 18}
print(person)

