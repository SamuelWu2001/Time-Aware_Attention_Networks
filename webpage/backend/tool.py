observatation=['467410 臺南','467420 永康','C0O930 玉井','C0O950 安南','C0O960 崎頂','C0O970 虎頭埤','C0O980 新市',
'C0O990 媽廟','C0O810 曾文','C0O830 北寮','C0O840 王爺宮','C0O860 大內','C0O900 善化','C0X050 東河','C0X060	下營',
'C0X080	佳里','C0X100 臺南市北區','C0X110 臺南市南區','C0X120 麻豆','C0X130	官田','C0X140 西港','C0X150	安定',
'C0X160 仁德','C0X170 關廟','C0X180	山上','C0X190 安平','C0X200 左鎮','C0X210 白河','C0X220 學甲','C0X230 鹽水',
'C0X240	關子嶺','C0X250	新營','C0X260 後壁','C0X280	將軍','C0X290 北門','C0X300 鹿寮','C0V630 茄萣','C0V640	湖內',
'C1V530	阿蓮','C0V370 古亭坑','C0V360 內門','C0V250	甲仙','C0V820 小林','C0V750	路竹','C0V530 阿蓮','C0V620	永安',
'C0V650 彌陀','C0V400 阿公店','C0V660 岡山','C1V390	尖山','C0V740 旗山','C0V310	美濃','C0V260 月眉','C0V800	六龜',
'C1V590	新發','C1V231 高中']

obs_lon=[120.204772,120.236700,120.460550,120.144861,120.369317,120.347878,120.298197,120.293525,
120.497328,120.495008,120.400850,120.360830,120.297219,120.385608,120.256261,120.145086,120.194228,
120.188378,120.248611,120.315422,120.203108,120.227839,120.257689,120.327797,120.363253,120.152181,
120.408522,120.414427,120.182187,120.247641,120.508025,120.316698,120.362326,120.135770,120.125481,
120.477331,120.182608,120.244500,120.401947,120.466769,120.591758,120.633250,120.259439,120.327508,
120.236856,120.246361,120.355528,120.294958,120.367789,120.483597,120.519153,120.539853,120.633583,
120.646064,120.716711]

obs_lat=[22.993239,23.038386,23.126042,23.076694,22.959547,23.021375,23.061614,22.991750,23.219681,
23.079561,23.222064,23.118850,23.112883,23.296598,23.226950,23.173039,23.010394,22.961189,23.183289,
23.193217,23.125608,23.102614,22.968258,22.963017,23.075700,22.993161,23.056758,23.347466,23.230367,
23.272621,23.331169,23.310712,23.366358,23.214999,23.267772,23.386047,22.906642,22.887139,22.893178,
22.975481,23.080106,23.148408,22.854997,22.883208,22.823150,22.783806,22.804194,22.797078,22.813153,
22.888614,22.898742,22.971003,22.997889,23.057019,23.134911]

t_minute=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17',
'18','19','20','21','22','23','24']

import requests
from bs4 import BeautifulSoup
from math import radians, cos, sin, asin, sqrt 
import datetime
from urllib.parse import quote
import numpy as np


def distance(lon1, lat1, lon2, lat2): 
    # 將十進位制度數轉化為弧度 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) 
    # haversine公式 
    dlon = abs(lon2 - lon1) 
    dlat = abs(lat2 - lat1) 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球平均半徑，單位為公里 
    return c * r * 1000

def find_weather(addnum,stname,date,date_p,T):     #找天氣
    temp_humid =[] 
    while True:
        try:
            url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station="+ addnum +"&stname=" + stname +"&datepicker=" + date_p+"&altitude=0m"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find('table',{'id':'MyTable'})    
            for t in t_minute:
                temp = table.find(text=t).findNext('td').findNext('td').findNext('td').text.replace('\xa0','')
                humid = table.find(text=t).findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.replace('\xa0','')
                temp_humid.append((temp ,humid))
            break
        except:
            continue
    while True:
        try:
            url = "https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station="+ addnum +"&stname=" + stname +"&datepicker=" + date+"&altitude=0m"
            #print(url)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find('table',{'id':'MyTable'})
            for t in t_minute:
                temp = table.find(text=t).findNext('td').findNext('td').findNext('td').text.replace('\xa0','')
                humid = table.find(text=t).findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.replace('\xa0','')
                temp_humid.append((temp ,humid))
            break
        except:
            continue
    return temp_humid[T:T+24]

def find_obsv(lon,lat,date_time):        #找最近觀測站
    dis = []
    for i in range(len(obs_lat)):
        dis.append(distance(lon,lat,obs_lon[i],obs_lat[i]))
    while True:  
        if dis==None:
            return None
        temp = min(dis)
        index = dis.index(temp)
        add = observatation[index].split(' ')
        time = date_time.split(' ')
        time[1] = int(time[1][:-3])
        time[0] = time[0].replace('/','-')
        previous = datetime.datetime.strptime(time[0],"%Y-%m-%d")
        time[0] = previous
        time[0] = str(time[0]).split(" ")[0]
        previous = previous - datetime.timedelta(days = 1)
        previous = str(previous).split(" ")[0]
        try:
            w = find_weather(add[0],quote(quote(add[1])),time[0],previous,time[1])
            #print( w.count(('/','/')))
            if w.count('/')+w.count('...')+w.count('X')<=2:
                break
            else:
                dis.remove(temp)
                continue
        except:
            dis.remove(temp)
            continue
        
        #else:       
        #    dis.remove(temp)
    return w