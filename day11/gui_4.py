import tkinter
# Python GUI 視窗建立
# 建構小視窗 + Label 標籤文字 + Button 按鈕與事件
# +----------+
# | My Clock |
# +----------+
# | 15:03:32 |  <-- 時間會自己跳動
# |   Exit   |
# +----------+


def win_exit():
    win.quit()


if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('My Clock')
    win.geometry('500x250')

    data = tkinter.StringVar()  # 建立一個 tkinter 的可變字串
    data.set('00:00:00')  # 設定 data 的內容
    time_label = tkinter.Label(win, textvariable=data, fg='blue', font=('Arial', 80))
    time_label.pack()

    exit_button = tkinter.Button(win, text='Exit', font=('Arial', 80), command=win_exit)
    exit_button.pack()

    win.mainloop()
