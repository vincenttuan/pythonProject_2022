import tkinter
from tkinter import messagebox
# Python GUI 視窗建立
# 建構小視窗 + Label 標籤文字 + Button 按鈕與事件
# +----------+
# | MyWindow |
# +----------+
# |  Hello   |
# | OK  Exit |
# +----------+


def show_msg():
    messagebox.showinfo('我的小視窗', 'I Love Python')


def win_exit():
    win.quit()  # 視窗關閉


if __name__ == '__main__':
    win = tkinter.Tk()
    win.title('MyWindow')
    win.geometry('300x300')
    # Label 元素配置
    label = tkinter.Label(win, text='Hello', bg='yellow', font=('Arial', 20), width=30, height=5)
    label.pack()
    # Button 元素配置
    btn1 = tkinter.Button(win, text="OK", font=('Arial', 20), width=10, height=5, command=show_msg)
    btn2 = tkinter.Button(win, text="Exit", font=('Arial', 20), width=10, height=5, command=win_exit)
    btn1.pack(side=tkinter.LEFT)
    btn2.pack(side=tkinter.RIGHT)
    win.mainloop()
