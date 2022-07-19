"""
Date: 18.12.18
url: https://blog.naver.com/dsz08082/221422018070
Tkinter # 4. Radiobutton
- Radiobutton, StringVar, IntVar
"""

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("language") # 프로그램에 맞게
root.geometry("300x170") # 타이틀과 화면크기 조정
root.resizable(0,0)

def your_choice():
	yn = 'not selected' # 아무것도 선택하지 않을 경우를 대비해 기본 값을 선택 안함으로 둠.
	if Radiovar.get() == 1: # Radiovar.get()은 선택된 항목에 맞게 가져온 값임.
		yn = "Java selected" # 각 경우에 맞는 메시지로 바인딩(변수에 할당).
	elif Radiovar.get() == 2:
		yn = "Python selected"
	elif Radiovar.get() == 3:
		yn = "C Languages selected"
	lbl2.configure(text="your choice: "+yn) #라벨 변경
	messagebox.showinfo("your choice",yn) #메시지 띄우기

lbl = Label(root, text="""The following items are popular\nprogramming languages.""", font="NanumGothic 10")
lbl.pack() # 라벨 생성 및 패킹, 문자열이 길기 때문에 중간에 개행함.

yn = StringVar() # 문자열 선언
Radiovar = IntVar() # 정수 선언

Radio_button1 = Radiobutton(text="Java",variable=Radiovar,value=1) # 라디오버튼 총 3개 선언
Radio_button2 = Radiobutton(text="Python",variable=Radiovar,value=2) # 각 텍스트, 상황값, 인덱스
Radio_button3 = Radiobutton(text="C Languages",variable=Radiovar,value=3) # 설정된 후 변수 선언
btn = Button(root, text="choice",command=your_choice,width=5,height=1)
lbl2 = Label(root,text="your choice : ")

Radio_button1.pack()
Radio_button2.pack()
Radio_button3.pack()
btn.pack()
lbl2.pack()

root.mainloop()