"""
tk_navernews.py
date. 21.02.01
by. @neltia / dsz08082@naver.com
"""
import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox

search = Tk()
search.title("네이버 뉴스 수집")
search.geometry("350x100")
search.resizable(False, False)


def func():
    time.sleep(0.5)

    cnt = int(Entry.get(count))
    keyword = Entry.get(display)
    count.delete(0,END)
    display.delete(0,END)

    myurls_title = []
    myurls_url = []
    myurls_source = []
    total = 1
    for index in range(1, cnt*10+1, 10):
        url =  f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={index}"

        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        myurls_title += soup.find_all('a', class_='news_tit')
        myurls_url += soup.find_all('a', class_='news_tit')
        myurls_source += soup.find_all('a', class_='info press')
        total +=1
        time.sleep(0.5)

    # stats.configure(text="상태: 수집 완료")
    myurls_text_title = [myurl_title.attrs['title'] for myurl_title in myurls_title]
    myurls_text_url = [myurl_url.attrs['href'] for myurl_url in myurls_url]
    myurls_text_source = [myurl_source.text.replace("언론사 선정","") for myurl_source in myurls_source]

    myurls_text = [myurls_text_title] + [myurls_text_url] + [myurls_text_source]

    myurls_text_reshape = np.transpose(myurls_text)

    news_search = pd.DataFrame(myurls_text_reshape)
    news_search.columns = ['제목','URL','언론사']
    news_search = news_search.set_index('제목')
    news_search.to_excel('news_{}.xlsx'.format(keyword))
    messagebox.showinfo("성공", "엑셀 파일 추출이 완료 되었습니다.")


# Menu Items
label1 = Label(search, text="페이지 수")
label1.grid(row=1, column=0)

count = Entry(search, width=20)
count.grid(row=1, column=1)

label2 = Label(search, text="(단위: 페이지당 10)")
label2.grid(row=1, column=2)

label3 = Label(search, text="검색어")
label3.grid(row=2, column=0)

display = Entry(search, width=20)
display.grid(row=2, column=1)

# stats = Label(search, text="상태: 대기중")
# stats.grid(row=3, column=0)

btn = Button(search, text="확인", command=func) # btn.bind('<Button-1>', func)
btn.grid(row=3, column=2)

search.mainloop()
