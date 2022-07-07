# 使用者輸入應用
# BMI 計算
# 使用者輸入 身高(h), 體重(w) 求 bmi = ?
h = input('請輸入身高(cm): ')
print(h, type(h))
h = float(h)  # 將 h 轉為 float 浮點數
print(h, type(h))

w = float(input('請輸入體重(kg): '))
print(w, type(w))

bmi = w / (h/100)**2
print("bmi = %.2f" % bmi)

# bmi 判斷
# bmi <= 18 過輕
# bmi > 23 過重
# 18 < bmi <= 23 正常

if bmi <= 18:
    print('過輕')

if bmi > 23:
    print('過重')

if 18 < bmi <= 23:
    print('正常')

# 改良
if bmi <= 18:
    print('過輕')
elif bmi > 23:
    print('過重')
else:
    print('正常')

# 精簡寫法
result = '過輕' if bmi <= 18 else '過重' if bmi > 23 else '正常'
print(result)
