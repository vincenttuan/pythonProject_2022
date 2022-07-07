# 英文繞口令
words = 'she sell sea shell on the sea shore'
print(words)
print('字數:', len(words))
print('有幾個 sea:', words.count('sea'))
print('有幾個 s:', words.count('s'))
print('是否都是 A-Z a-z 不含空白的連續英文字:', words.isalpha())
array = words.split()  # 利用空白" "來切出共有多少單字
print(array)  # ['she', 'sell', 'sea', 'shell', 'on', 'the', 'sea', 'shore']
print('單字數:', len(array))
print('words 中有無 shell 這個字：', words.find('shell'))
# words.find(keyword) 若沒有找到指定 keyword 則會傳回 -1
print('words 中有無 shell 這個字：', '沒有' if words.find('shell') == -1 else '有')
