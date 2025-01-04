import tkinter as tk

def checkbutton_click():
    if is_show_pass_word.get():
        entry_pass_word["show"] = ""
    else:
        entry_pass_word["show"] = "*"
def button_login_click():
    if user_name.get()=="root" and pass_word.get()=="admin":
        label_header["text"] = "登陆成功"
        label_header["bg"] = "black"

    else:
        user_name.set("")
        pass_word.set("")
        label_header["text"] = "用户密码错误，请重新输入"
        label_header["bg"] = "red"
def button_exit_click():
    win.quit()
def centerWin(win):
    win.update()
    sw,sh = win.winfo_screenwidth(),win.winfo_screenheight()
    rw, rh = win.winfo_width(), win.winfo_height()
    print(sw,sh,rw,rh)
    win.geometry("+%d+%d"%((sw-rw)/2,(sh-rh)/2))
      
if __name__ == '__main__':
    win = tk.Tk()

    win.title("登录")

    user_name = tk.StringVar()
    pass_word = tk.StringVar()
    is_show_pass_word = tk.BooleanVar()
    is_show_pass_word.set(False)

    label_header = tk.Label(win, text="请登录")
    label_header.grid(row = 0,column = 0,columnspan=2)

    label_user_name =tk.Label(win,text = "用户名:")
    label_pass_word =tk.Label(win,text = "密码:")
    entry_user_name = tk.Entry(win,textvariable=user_name)
    entry_pass_word = tk.Entry(win,textvariable=pass_word,show="*")

    label_user_name.grid(row = 1,column = 0,padx = 5,pady = 5)
    label_pass_word.grid(row = 2,column = 0,padx = 5,pady = 5)
    entry_user_name.grid(row = 1,column = 1,padx = 5,pady = 5)
    entry_pass_word.grid(row = 2,column = 1,padx = 5,pady = 5)

    checkbutton_show_passwd = tk.Checkbutton(win,text="显示密码",variable=is_show_pass_word,command=checkbutton_click)
    checkbutton_show_passwd.grid(row =3,column = 0,padx = 5,pady = 5)

    button_login = tk.Button(win, text="登录",command=button_login_click)
    button_exit = tk.Button(win, text="退出", command=button_exit_click)
    button_login.grid(row=4,column = 0,padx=5)
    button_exit.grid(row=4, column=1, padx=5)

    win.mainloop()