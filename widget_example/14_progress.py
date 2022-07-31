"""
Date: 22.07.30
url: https://blog.naver.com/dsz08082/222834875493
Tkinter # 14. progress bar
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

window = tk.Tk()
window.geometry("200x150")
window.resizable(False, False)

# 사용 형식
# - 진행 막대가 계속 움직이도록
"""
progressbar = ttk.Progressbar(window, maximum=100, mode="indeterminate")
progressbar.pack()
progressbar.start(30)

window.mainloop()
"""

# 사용 예시
# - 반복문을 통한 진행 상태 설정
def loop_test():
    btn['state'] = tk.DISABLED

    end_point = 100000
    for idx in range(end_point):
        current_var.set(idx/end_point * 100)
        progress_bar.update()

    messagebox.showinfo("성공", "완료되었습니다!")

    btn['state'] = tk.NORMAL
    current_var.set(0)
    progress_bar.update()


current_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(window, variable=current_var, maximum=100)
progress_bar.pack()

btn = tk.Button(window, text="Test", command=loop_test)
btn.pack()

window.mainloop()
