"""
Date: 19.12.23
url: https://blog.naver.com/dsz08082/221746475738
Tkinter # 10. filedialog
"""

from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("call directory")
root.geometry("540x300+100+100")
root.resizable(False, False)


def ask():
    root.dirName=filedialog.askdirectory()
    print(root.dirName)
    # root.file = filedialog.askopenfile(initialdir='path', title='select file', filetypes=(('jpeg files', '*.jgp'), ('all files', '*.*')))
    txt.configure(text="pwd: " + root.dirName)


def ask1():
    root.file = filedialog.askopenfile(
    initialdir='path',
    title='select file',
    filetypes=(('png files', '*.png'),
        ('all files', '*.*')))

    txt.configure(text="pwd: " + root.file.name)


lbl = Label(root, text="pwd")
lbl.pack()

txt = Label(root, text=" ")
txt.pack()

btn = Button(root, text="ask",command=ask)
btn.pack()

root.mainloop()
