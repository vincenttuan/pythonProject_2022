# 1. lambda parameter_list: expression
max_func = lambda a, b: a if a > b else b
max_value = max_func(10, 20)
print(max_value)

# 2. (lambda parameter_list: expression)(argument)
result_value = (lambda x: x*x-x)(5)
print(result_value)

# 3. filter(lambda parameter_list: expression, iterable)
# iterable 數組


# 4. map(lambda parameter_list: expression, iterable)
# map 轉換


# 5. reduce(lambda param1, param2: expression, iterable)
# reduce 歸納


# 6. sorted(iterable, key=lambda parameter_list: expression)


