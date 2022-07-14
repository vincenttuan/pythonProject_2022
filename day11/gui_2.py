import tkinter
# Python GUI 視窗建立
# 建構小視窗 + Label 標籤文字
# +----------+
# | MyWindow |
# +----------+
# |  Label   |
# |          |
# +----------+

if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('MyWindow')
    win.geometry('300x300')
    # Label 元素配置
    label = tkinter.Label(
        win,
        text='Hello',
        bg='yellow',
        font=('Arial, 20'),
        width=30,
        height=5
    )
    label.pack()  # 裝配到指定 GUI 中
    win.mainloop()
