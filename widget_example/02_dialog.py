"""
Date: 18.12.16
url: https://blog.naver.com/dsz08082/221420030583
Tkinter # 2. new dialog
- title, label, entry, button, pack
"""

from tkinter import *
root = Tk()
root.title("blog")
root.geometry("200x100")
root.resizable(0,0)

def your_name():
	print("Hello!")

lbl = Label(root, text="name", font="NanumGothic 15")
lbl.pack()

txt = Entry(root)
txt.pack()

btn = Button(root, text="ok",command=your_name)
btn.pack()

root.mainloop()
