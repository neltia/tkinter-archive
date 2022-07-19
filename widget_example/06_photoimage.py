"""
Date: 18.12.20
url: https://blog.naver.com/dsz08082/221422878011
Tkinter # 6. PhotoImage
"""

from tkinter import *


# 클래스 정의
class MyFrame(Frame):
    def __init__(self, master):
        img = PhotoImage(file='user.png') # 이미지 읽고
        lbl = Label(image=img) # 이미지 넣어
        lbl.image = img  # 레퍼런스 추가
        lbl.pack()


# 메인함수로 정의
def main():
    root = Tk()
    root.title('이미지 보기')
    root.geometry('500x400+10+10')
    MyFrame(root) # 클래스 사용
    root.mainloop()

# 메인함수 호출
if __name__ == '__main__':
    main()
