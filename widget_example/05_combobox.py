"""
Date: 18.12.19
url: https://blog.naver.com/dsz08082/221422153757
Tkinter # 5. ttk.Combobox
"""

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("blog")
root.geometry("220x150")
root.resizable(0,0)

def click():
	cl = strs.get()
	cl2 = strs2.get()
	lbl4.configure(text="your age: "+cl+"\n"+"your gen: "+cl2)

strs = StringVar() #변수선언
strs2 = StringVar()

lbl = Label(root,text="imformation program!")
lbl.grid(row=0,column=1)

lbl2 = Label(root, text="age", font="NanumGothic 10")
lbl2.grid(row=1, column=0)

Combx1 = ttk.Combobox(textvariable=strs, width=20) # 콤보박스 선언
Combx1['value'] = ('10대','20대','30대','40대') # 콤보박스 요소 삽입
Combx1.current(0) # 0번째로 콤보박스 초기화
Combx1.grid(row=1,column=1) # 콤보박스 배치

lbl3 = Label(root, text="gen", font="NanumGothic 10")
lbl3.grid(row=3, column=0)

Combx2 = ttk.Combobox(textvariable=strs2, width=20)
Combx2['value'] = ('남자','여자')
Combx2.current(0)
Combx2.grid(row=3,column=1)

btn = Button(root, text="check",command=click,width=6,height=1)
btn.grid(row=4,column=1)

lbl4 = Label(root, text="imformation", font="NanumGothic 11")
lbl4.grid(row=5, column=1)
print(type(strs))
root.mainloop()
