import tkinter
# Python GUI 視窗建立
# 建構小視窗 + Label 標籤文字 + Button 按鈕與事件
# +----------+
# | My Clock |
# +----------+
# | 15:03:32 |  <-- 時間會自己跳動
# |   Exit   |
# +----------+

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('My Clock')
    win.geometry('300x300')
    data = tkinter.StringVar  # 建立一個 tkinter 的可變字串
    time_label = tkinter.Label(win, textvariable=data, fg='blue', font=('Arial', 80))
    win.mainloop()
