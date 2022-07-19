"""
Date: 21.02.02
url: https://blog.naver.com/dsz08082/222229126747
Tkinter # 13. event binding
- font, event
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x150")


def your_name(event):
	yn = txt.get()
	txt.delete(0,END)
	messagebox.showinfo("name",yn)


def keyPressed(event):
    lbl.configure(text="입력한 키: " + event.char)


lbl = Label(root, text="name")
lbl.pack()

txt = Entry(root)
txt.pack()

btn = Button(root, text="Double Click!")
btn.bind("<Double-Button-1>", your_name)
btn.pack()

frame = Frame(root, width=100, height=100)
lbl = Label(frame, text="") # 입력 키 표시
lbl.pack()
frame.bind('<Key>', keyPressed) # 이벤트 바인딩
frame.pack()

lbl = Label(frame, text="입력한 키: ") # 입력 키 표시
lbl.pack()

frame.focus_set() # 키보드 포커스를 맞춤

root.mainloop()

