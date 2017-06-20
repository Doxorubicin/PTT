# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:58:01 2017

@author: Doxorubicin
"""

from bs4 import BeautifulSoup
import time


def data(r=0):

    # 網頁(html)在入soup中
    soup = BeautifulSoup(r, 'lxml')
    ddata = soup.find_all(class_ = 'article-meta-value')
        
    #[<span class="article-meta-value">bgworld (solid)</span>, <span class="article-meta-value">ac_in</span>, <span class="article-meta-value">[洽特] 路線擬人化</span>, <span class="article-meta-value">wed jun 18 07:41:36 2014</span>]
    
    board = 0
    
    #因為句子是逐行出現，所以只好這樣子土法煉鋼，讓它一次一次的對應。
    number = 1
    for div in ddata:
        pddata = div.get_text()
        if number == 1:
            author = pddata
        elif number == 2:
            board = pddata
        elif number == 3:
            title = pddata
        elif number == 4:
            clock = pddata
        number = number + 1
        
    #Python時間處理完全手冊
    trans = clock
    struct_time = time.strptime(trans,'%a %b %d %H:%M:%S %Y')
    clock =  time.strftime('%Y-%m-%d(%a)%H-%M-%S',struct_time)
    
    #這是因為windows有些字元不能當檔名
    #replace的用法
    #\\	表示反斜線\
    title = title.replace('*','＊')
    title = title.replace('|','｜')
    title = title.replace('\\','＼')
    title = title.replace(':','：')
    title = title.replace('"','＂')
    title = title.replace('<','＜')
    title = title.replace('>','＞')
    title = title.replace('?','？')
    title = title.replace('/','／')  
    author = author.replace('*','＊')
    author = author.replace('|','｜')
    author = author.replace('\\','＼')
    author = author.replace(':','：')
    author = author.replace('"','＂')
    author = author.replace('<','＜')
    author = author.replace('>','＞')
    author = author.replace('?','？')
    author = author.replace('/','／')
    
    #檢查頁面是否還存在
    if board == 0:
        out =  "error:下面的網址已經404：" + time.strftime("%h:%m:%s")
        with open('z:\\log.txt', 'a', encoding='utf-8') as log:
            print(out, file=log)
        raise ('網頁已經404')        
    else:
        author = "【" + author + "】"
        board = "【" + board + "】"
        title = title
        clock = "【" + clock + "】"
        name = clock + board + title + author
        
        file = "z:\\postPTT\\" + name + ".html"
        out =  r
        #open的指令用w，新建檔案寫入(檔案可不存在，若存在則清空)
        with open(file, 'w', encoding='utf-8') as log:
            print(out, file=log)  
    return
    