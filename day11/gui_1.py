import tkinter
# Python GUI 視窗建立
# 建構小視窗
# +----------+
# | MyWindow |
# +----------+
# |          |
# |          |
# +----------+

if __name__ == '__main__':
    win = tkinter.Tk()  # 取得視窗物件
    win.title('MyWindow')  # 設定視窗抬頭
    win.geometry('300x300')  # 設定視窗大小
    win.mainloop()  # 視窗運行

