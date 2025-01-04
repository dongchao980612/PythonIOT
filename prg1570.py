import tkinter as tk


def centerWin(win):
    win.update()
    sw,sh = win.winfo_screenwidth(),win.winfo_screenheight()
    rw, rh = win.winfo_width(), win.winfo_height()
    print(sw,sh,rw,rh)
    win.geometry("+%d+%d"%((sw-rw)/2,(sh-rh)/2))

if __name__ == '__main__':
    win = tk.Tk()

    centerWin(win)
    win.title("登录")

    label_user_name =tk.Label(win,text = "用户名")
    label_pass_word =tk.Label(win,text = "密码")
    entry_user_name = tk.Entry(win)
    entry_pass_word = tk.Entry(win)
    label_user_name.grid(row = 0,column = 0,padx = 5,pady = 5)
    label_pass_word.grid(row = 1,column = 0,padx = 5,pady = 5)
    entry_user_name.grid(row = 0,column = 1,padx = 5,pady = 5)
    entry_pass_word.grid(row = 1,column = 1,padx = 5,pady = 5)
    button_login = tk.Button(win,text = "登录")
    button_login.grid(row=2,column = 0,columnspan=2,padx=5,pady=5)

    win.mainloop()