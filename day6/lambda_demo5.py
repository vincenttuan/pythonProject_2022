# lambda 與 dict 字典數組的應用
computer = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

result = computer.get('+')(20, 10)
print(result)

result = computer.get('!', lambda x, y: None)(20, 10)
print(result)
