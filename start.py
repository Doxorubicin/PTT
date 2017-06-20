# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 18:23:11 2017

@author: ATPX4869
"""


import requests
import time
import merge

def get_web_page(url):
    #避免網站block掉機器人的流量
    time.sleep(timeout)
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        out = str(count) + "："  + url + "下載失敗404-" + time.strftime("%H:%M:%S")
        with open('Z:\\log.txt', 'a', encoding='UTF-8') as log:
            print(out, file=log)
        return None
    else:
        return resp.text

timeout = 0.5
count = 1

file = open("Z:\\weblist.txt","r")
urlList = file.readlines()
#行數
lines = len(urlList)
for url in urlList:
    #進度
    state = "（" + str(count) + "/" + str(lines) + "）"
    #剩下幾次
    poststate = lines - count
    #還有多久(秒)
    postsecond = poststate * timeout
    #時間轉換
    minute, second = divmod(postsecond, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    
    #進度
    state = "（" + str(count) + "/" + str(lines) + "）"
    #剩下幾次
    poststate = lines - count
    #還有多久(秒)
    postsecond = poststate * timeout
    #時間轉換
    minute, second = divmod(postsecond, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    
    second = int(second)
    minute = int(minute)
    hour = int(hour)
    day = int(day)
    
    #時間統整
    if day == hour == minute == 0:
        posttime = "還剩下：" + str(second) + "秒"
    elif day == hour == 0:
        posttime = "約：" + str(minute) + "分" + str(second) + "秒"
    elif day == 0:
        posttime = "約：" + str(hour) + "時" + str(minute) + "分" + str(second) + "秒"
    else:
        posttime = "約：" + str(day) + "天" + str(hour) + "時" + str(minute) + "分" + str(second) + "秒"
    #公告
    print ("目前進度：" + state + "還剩下" + str(poststate) + "次，" + posttime)
    count = count + 1
    """把字串中的\n(換行)給剔除"""
    url=url.strip('\n')
    try:
        r = get_web_page(url)
        out = r
        merge.data(out)
    except:
        out = str(count) + "：" + url + "下載失敗-" + time.strftime("%H:%M:%S")
        with open('Z:\\log.txt', 'a', encoding='UTF-8') as log:
            print(out, file=log)
    else:
        out = str(count) + "："  + url + "下載成功-" + time.strftime("%H:%M:%S")
        with open('Z:\\log.txt', 'a', encoding='UTF-8') as log:
            print(out, file=log)