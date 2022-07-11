# 定義攝氏轉華氏 ctof、華氏轉攝氏 ftoc
def ctof(c):
    f = c * (9/5) + 32
    return f

def ftoc(f):
    c = (f - 32) * (5/9)
    return c

if __name__ == '__main__':
    c = 10.5
    print('攝氏: %.1f 華氏: %.1f' % (c, ctof(c)))
    f = 80
    print('華氏: %.1f 攝氏: %.1f' % (f, ftoc(f)))

