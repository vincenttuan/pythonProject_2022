# 字串索引 []
word = 'Hello Python'
print(word)
print(word[0], word[1], word[2], word[3], word[4])
print(word[-1], word[-2], word[-3], word[-4])
# 取出 lo Py
print(word[3:8])  # 3<=index<8
print(word[3:])   # 從3的位置開始取，取到結尾
print(word[:8])   # 從頭取到 < 8 的位置
