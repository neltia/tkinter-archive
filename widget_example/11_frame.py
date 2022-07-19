"""
Date: 20.12.04
url: https://blog.naver.com/dsz08082/222161918101
Tkinter # 11. frmae
"""

from tkinter import *

root = Tk()
root.title("Neltia")
root.geometry("400x400")
root.resizable(False, False)

frame1 = Frame(root, relief="solid", bd=2)
frame1.pack(side="top", fill="both", expand=True)

frame2 = Frame(root, relief="solid")
frame2.pack(side="bottom", fill="both", expand=True)

lbl = Label(frame1, text="플레이어")
lbl.pack(side="bottom")

button1 = Button(frame2, text="프레임2: ^")
button1.pack()

button2 = Button(frame2, text="프레임2: <")
button2.pack(side="left")

button2 = Button(frame2, text="프레임2: >")
button2.pack(side="right")

"""
frame1 = Frame(root)
frame1.pack(side="top", fill="both", expand=True)

frame2 = Frame(root)
frame2.pack(side="bottom", fill="both", expand=True)

button1 = Button(frame1, text="프레임1: ^")
button1.pack()

lbl = Label(frame1, text="플레이어")
lbl.pack(side="bottom")

button2 = Button(frame2, text="프레임2: <")
button2.pack(side="left")

button2 = Button(frame2, text="프레임2: >")
button2.pack(side="right")
"""

root.mainloop()
