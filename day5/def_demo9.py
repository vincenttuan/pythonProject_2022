# 請試做一個 def calcBmi 方法
# calcBmi 方法可以輸入 2 個參數(分別是身高與體重)
# 回傳 bmi 值 與 bmi 是否正常、過重、過輕 (18<bmi<=23 正常範圍)
# 有三組測試資料 170, 50 ; 180, 70 ; 160, 60
import math

# 研判 bmi 正常、過重、過輕
def getBmiInfo(bmi):
    if bmi <= 18:
        return "過輕"
    elif bmi > 23:
        return "過重"
    else:
        return "正常"

# 計算 bmi 值
def calcBmi(h, w):
    bmi_value = w / math.pow(h/100, 2)
    bmi_info = getBmiInfo(bmi_value)
    return bmi_value, bmi_info


if __name__ == '__main__':
    bmiValue, bmiInfo = calcBmi(170, 50)
    print('BMI: %.2f Info: %s' % (bmiValue, bmiInfo))
    bmiValue, bmiInfo = calcBmi(180, 70)
    print('BMI: %.2f Info: %s' % (bmiValue, bmiInfo))
    bmiValue, bmiInfo = calcBmi(160, 60)
    print('BMI: %.2f Info: %s' % (bmiValue, bmiInfo))
