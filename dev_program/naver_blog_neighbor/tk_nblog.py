"""
tk_nblog.py
date. 22.07.19
by. @neltia / dsz08082@naver.com
"""
# crawling lib
from click import progressbar
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
from pytz import timezone
from datetime import datetime
import sys
# gui - tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

# set tkinter
searcher = Tk()
searcher.title("네이버 블로그 이웃 목록 수집")
searcher.geometry("425x140")
searcher.resizable(False, False)


def main_crawling():
    btn_down['state'] = DISABLED
    time.sleep(0.1)

    driver = driver_setting()
    stat, blogger_id, blogger_name_list, blog_url_list = data_parsing(driver)
    if stat == -1:
        crawling_complete(stat)
        return
    excel_download(blogger_id, blogger_name_list, blog_url_list)
    crawling_complete(stat)


# selenium driver setting
def driver_setting():
    # driver setting
    options = Options()
    # - user agent
    user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.36"
    options.add_argument(user_agent)
    # - headless: 크롤링 시 웹 드라이버의 브라우저가 화면에 열리지 않고 백그라운드로 진행
    options.add_argument("headless")
    # - 드라이버 수행
    driver = webdriver.Chrome("chromedriver", options=options)
    driver.implicitly_wait(3)
    return driver


# data crawling with selenium & bs4
def data_parsing(driver):
    stat = 0

    # input data
    blogger_id = Entry.get(naver_id)
    try:
        subscr_cnt = int(Entry.get(subscriber_cnt))
    except ValueError:
        stat = -1
        return stat, "", "", ""
    idx_rng = subscr_cnt // 20 + 1

    # data parsing
    blog_url_list = []
    blogger_name_list = []
    for idx in range(1, idx_rng+1):
        get_url = f"https://section.blog.naver.com/connect/ViewMoreFollowers.naver?blogId={blogger_id}&currentPage={idx}"
        driver.get(get_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        link_list = soup.find_all('a', class_="buddy_name")
        for link in link_list:
            blog_url = link["href"].strip()
            blogger_name = link.text.strip()

            blog_url_list.append(blog_url)
            blogger_name_list.append(blogger_name)

        print(f"{idx} page completed")
        current_var.set(idx/idx_rng * 100)
        progress_bar.update()
        time.sleep(0.5)
    driver.quit()
    return 0, blogger_id, blogger_name_list, blog_url_list


# crawling data 2 excel file
def excel_download(blogger_id, blogger_name_list, blog_url_list):
    # pandas의 Dataframe을 활용하여 데이터 파싱
    pre_dict = {'blogger': blogger_name_list, 'blog_url': blog_url_list}
    df = pd.DataFrame(pre_dict)
    df["mail_address"] = [f"{url.split('/')[-1]}@naver.com" for url in df["blog_url"]]
    df.index += 1

    # export excel
    now_date = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
    df.to_excel(f"blog_{blogger_id}_{now_date}.xlsx")
    return


# crawling complete
def crawling_complete(stat):
    if stat == -1:
        messagebox.showinfo("실패", "네이버 블로그 이웃 수는 숫자 값만 입력해야 합니다.")
    else:
        messagebox.showinfo("성공", "엑셀 파일 추출이 완료 되었습니다.")
    btn_down['state'] = NORMAL
    current_var.set(0)
    progress_bar.update()


# Menu Items
by_mail = Label(searcher, text="by dsz08082@naver.com")
by_mail.grid(row=0, column=2)

description_id = Label(searcher, text="네이버 아이디")
description_id.grid(row=1, column=0)

naver_id = Entry(searcher, width=20)
naver_id.grid(row=1, column=1)

description_count = Label(searcher, text="네이버 블로그 이웃 수")
description_count.grid(row=2, column=0)

subscriber_cnt = Entry(searcher, width=20)
subscriber_cnt.grid(row=2, column=1)

padding = Label(searcher, text="")
padding.grid(row=3, column=1)

description_progress = Label(searcher, text="진행 상태:")
description_progress.grid(row=4, column=0)

current_var = DoubleVar()
progress_bar = ttk.Progressbar(searcher, variable=current_var, maximum=100)
progress_bar.grid(row=5, column=0)

btn_down = Button(searcher, text="Excel Report 다운로드", command=main_crawling) # btn.bind('<Button-1>', func)
btn_down.grid(row=5, column=2)

searcher.mainloop()
