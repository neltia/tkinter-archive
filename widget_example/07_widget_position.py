"""
Date: 18.12.21
url: https://blog.naver.com/dsz08082/221423190999
Tkinter # 7. widget position
# - pack, grid, place
"""

from tkinter import *

root = Tk()
root.title("blog")
root.geometry("200x100")
root.resizable(0,0)

lbl = Label(root, text="test", font="NanumGothic 15")
lbl.pack()
# lbl.grid(row=0, column=1)

txt = Entry(root)
txt.pack()
# txt.grid(row=1, column=1)

x, y = 2, 1
btn = Button(root, text=str(x)+"x"+str(y),width=x,height=y)
btn.pack()
# btn.grid(row=2, column=0)
btn2 = Button(root, text=str(x)+"x"+str(y),width=x,height=y)
btn2.pack()
# btn2.grid(row=4, column=1)
# btn3 = Button(root, text=str(x)+"x"+str(y),width=x,height=y)
# btn3.grid(row=6, column=2)
# btn2 = Button(root, text="(0,0"), width=x, height=y)
# btn2.place(x=0, y=0)

root.mainloop()
