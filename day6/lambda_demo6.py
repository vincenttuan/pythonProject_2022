from functools import reduce

# 1. lambda parameter_list: expression
max_func = lambda a, b: a if a > b else b
max_value = max_func(10, 20)
print(max_value)

# 2. (lambda parameter_list: expression)(argument)
result_value = (lambda x: x*x-x)(5)
print(result_value)

# 3. filter(lambda parameter_list: expression, iterable)
# iterable 數組
nums = [50, 2, 10, 40]
# 想要過濾出 >20 的資料
result = filter(lambda x: x > 20, nums)
print(list(result))  # 轉 list

# 4. map(lambda parameter_list: expression, iterable)
# map 轉換
scores = [50, 80, 90, 30]  # [False, True, True, False]
result = map(lambda x: x >= 60, scores)
print(list(result))

scores = [50, 80, 90, 30]  # [0, 1, 1, 0]
result = map(lambda x: 1 if x >= 60 else 0, scores)
print(list(result))

# 5. reduce(lambda param1, param2: expression, iterable)
# reduce 歸納
scores = [50, 80, 90, 30]
result = reduce(lambda x, y: x + y, scores)
# [50, 80, 90, 30]
# 第一次歸納: x=50, y=80: 130 <-- 下一次歸納的 x
# 第二次歸納: x=130, y=90: 220 <-- 下一次歸納的 x
# 第三次歸納: x=220, y=30: 250 <-- 歸納結束
print(result)

# 6. sorted(iterable, key=lambda parameter_list: expression)
# sorted 排序
scores = [50, 80, 90, 30]
scores = sorted(scores)  # 自然排序: 小 -> 大
print(scores)
scores = sorted(scores, reverse=True)  # 大 -> 小
print(scores)

# (座號, 分數)
#  [0]  [1]
scores = [(1, 90), (3, 80), (2, 100)]
# 依照座號排序
scores = sorted(scores)
print(scores)  # 預設會按照第一個值自然排序
# 依照分數排序且由大->小
scores = sorted(scores, key=lambda s: s[1], reverse=True)
print(scores)
