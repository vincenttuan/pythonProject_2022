# if elif else 判斷語句
score = 75
# 判定是否及格 ?
print(score >= 60)
# 一般寫法
if score >= 60:
    print('及格')
else:
    print('不及格')
# 精簡寫法
result = '及格' if score >= 60 else '不及格'
print(result)
