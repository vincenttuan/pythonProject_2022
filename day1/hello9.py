# 雞兔同籠
# 雞 + 兔 = 83
# 雞腳 + 兔腳 = 240
# 求雞(x),兔(y)各有幾隻?
amount = 83
feet = 240
'''
假設都是雞
83 * 2 = 166 雞腳
240 - 166 = 74 <-- 有兔子在其中
兔子是 4 隻腳算一隻
74 / (4-2) = 37 .. 兔子
83 - 37 = 46 .. 雞
'''
y = (feet - (amount * 2)) / 2
x = amount - y
print('雞: %d 兔子: %d' % (x, y))
