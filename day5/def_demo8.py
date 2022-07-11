# 全域變數與區域變數
x = 0  # x 是全域變數


# 在自訂方法中若要修改全域變數的內容，必須加入 global
def update(value):
    global x
    x = value  # x 指的就會是全域變數


if __name__ == '__main__':
    update(10)
    print(x)  # x 指的全域變數
