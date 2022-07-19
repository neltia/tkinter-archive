"""
Date: 18.12.30
url: https://blog.naver.com/dsz08082/221430582571
Tkinter # 8. load images
# - os listdir
"""

from tkinter import *
import os
path_dir = os.path.dirname(os.path.realpath(__file__))
file_list = os.listdir(path_dir)
real_file_list = [x for x in file_list if(x.endswith(".PNG") or (x.endswith(".png")==True))]
print(real_file_list)

xn=0
root=Tk()
root.title("blog")
root.geometry("700x550")
root.resizable(0, 0)
image=PhotoImage(file=real_file_list[xn])

def showimg():
	global xn
	global image
	xn+=1
	if(xn>=len(real_file_list)):
		xn=0
	image=PhotoImage(file=real_file_list[xn])
	label_2 = Label(root, image=image)
	label_2.place(x=0,y=150)

btn = Button(root,text="next",command=showimg,width=7,height=1)
btn2 = Button(root,text="previous",command=showimg,width=7,height=1)
label_1 = Label(root,text="My images!",font="NanumGothic 20")
label_2 = Label(root, image=image)
label_1.place(x=200,y=10)
label_2.place(x=0,y=150)
btn.place(x=300,y=50)
btn2.place(x=150,y=50)

print(xn)
root.mainloop()
