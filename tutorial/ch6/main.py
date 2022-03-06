# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter import ttk


def OpenFile():
    PathText.config(state=NORMAL)
    global IsFileOpen
    filename = filedialog.askopenfilename(filetypes = [("log file","*.log")])
    print(filename)
    if filename == "":
        IsFileOpen = False
    else:
        IsFileOpen = True
    print(IsFileOpen)
    PathText.delete(1.0,END)
    PathText.insert("insert",filename)
    PathText.config(state=DISABLED)

def Update():
    global IsFileOpen
    VersionTextStr = VersionText.get()
    print("version is ",VersionTextStr)
    if(VersionTextStr == ""):
        print("version is none")
    if(IsFileOpen == True and VersionTextStr != ""):
        SuccessMSG.set("成功!")
        print("升级成功！")
    else:
        SuccessMSG.set("失败!")
        print("升级失败！")
'''
def Updatl_sugar = ttk.Label(main,textvariable=var_sugar)
e():
    global IsFileOpen
    VersionTextStr = VersionText.get("0.0",END).split("\n")
    print("version is ",VersionTextStr)
    if(VersionTextStr[0] == ""):
        print("version is none")
    if(IsFileOpen == True and VersionTextStr[0] != ""):
        SuccessMSG.set("成功!")
        print("升级成功！")
    else:
        SuccessMSG.set("失败!")
        print("升级失败！")
'''
def click():
    # check['text']=var_sugar.get()
    print("ddd")

def cmd1():
    print(1)
    if v2.get()=="选中":
        v2.set('没选中')
    else:
        v2.set("选中")

window = Tk()
Tk.title(window,"日志分析工具")
Tk.geometry(window,"640x480")

Label(window,text = "文件路径:",font = ("KaiTi_GB2312",12)).grid(row = 0,column = 1,sticky = W)
PathText = Text(window,width = 50,height = 1)
PathText.grid(row = 0,column = 2,columnspan = 3)
Button(window,text = "打开文件",font = ("KaiTi_GB2312",12),command = OpenFile).grid(row = 0,column = 5,columnspan = 4,pady = 10)
Label(window,text = "软件版本:",font = ("KaiTi_GB2312",12)).grid(row = 2,column = 1,pady = 15,sticky = W)
VersionText = Entry(window,width = 16,font = ("KaiTi_GB2312",12))
#VersionText = Text(window,width = 16,height = 1,font = ("KaiTi_GB2312",12))
VersionText.grid(row = 2,column = 2,sticky = W)
SuccessMSG = Variable()
IsFileOpen = False
Label(window,textvariable = SuccessMSG,font = ("KaiTi_GB2312",12)).grid(row = 2, column = 4,columnspan = 4)
Button(window,text = "开始分析",font = ("KaiTi_GB2312",12),command = Update).grid(row = 2,column = 2,columnspan = 4)
Label(window,text = "分析结果:",font = ("KaiTi_GB2312",12)).grid(row = 2,column = 3,columnspan = 4)

Label(window,text = "图片路径:",font = ("KaiTi_GB2312",12)).grid(row = 3,column = 1,sticky = W)
PathImage = Text(window,width = 50,height = 1)
PathImage.grid(row = 3,column = 2,columnspan = 3)
Button(window,text = "打开文件",font = ("KaiTi_GB2312",12),command = OpenFile).grid(row = 3,column = 5,columnspan = 4,pady = 10)

Button(window,text = "开始分析",font = ("KaiTi_GB2312",12),command = Update).grid(row = 4,column = 2,columnspan = 4)
Label(window,text = "分析结果:",font = ("KaiTi_GB2312",12)).grid(row = 4,column = 3,columnspan = 4)


v = IntVar()
var_sugar = StringVar()
v2 = StringVar()
v2.set("没选中")

# C1 = Checkbutton(window, text = "选我试试",variable = v).pack()
# C1 = Label(window,textvariable = v)
# C1.grid(row = 5,column = 1,sticky = W)
main = ttk.Frame(window)

check=ttk.Checkbutton(main,text="点击事件",variable=v,onvalue="yes",offvalue="no",command=click)
# check = ttk.Checkbutton(main,text="选择一",variable=v2,onvalue="选中",offvalue="没选中",command=cmd1)

main.grid()
check.grid(column=0,row=5)

mainloop()
