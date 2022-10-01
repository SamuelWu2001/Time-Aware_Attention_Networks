#coding:utf-8
import requests
from requests.models import Response
from tqdm import tqdm
from fake_useragent import UserAgent 
import mysql.connector
from bs4 import BeautifulSoup
import multiprocessing as mp
import re
import numpy as np
import csv
from math import radians, cos, sin, asin, sqrt 
from urllib.parse import quote
import datetime
import time
ua = UserAgent()

#connection = mysql.connector.connect(host='140.116.247.183',
#                                    port='3306',
#                                    user='iir_undergrad',
#                                    password='iir_5757',
#                                    database='iir_undergrad'
#                                    )
#cursor = connection.cursor()
#cursor.execute("SET SQL_SAFE_UPDATES=0")
mapdict = {
'18327886':(120.20147205463435,23.00360070153901)}

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

perloc_dict = {}

def locate(address):
    map = mapdict.get(address)
    if map==None:
        return -1,-1
    else:
        return map[0],map[1]
    #if perloc_dict.get(address)!= None:
    #    return perloc_dict.get(address)[0],perloc_dict.get(address)[1]
    #else:
    #    try:
    #        response = requests.get("https://www.google.com/maps/place?q=" + address,headers={'User-Agent':ua.random})
    #        soup = BeautifulSoup(response.text, "html.parser")
    #        text = soup.prettify()
    #        init = text.find("window.APP_INITIALIZATION_STATE")
    #        data = text[init+35:init+77]  #將其後的參數進行存取
    #        loc = data.split(',')
    #        print(loc)
    #        if len(loc)>=3:
    #            longitude = float(loc[1])
    #            latitude = float(loc[2])
    #            perloc_dict[address]=(longitude,latitude)
    #        else:
    #            longitude = -1
    #            latitude = -1
    #    except:
    #        longitude = -1
    #        latitude = -1
    #    return longitude,latitude

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
            response = requests.get(url,headers={'User-Agent':ua.random})
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
            response = requests.get(url,headers={'User-Agent':ua.random})
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
            count = 0
            for i in range(len(w)):
                if w[i][0]=='...' or w[i][1]=='...' or w[i][0]=='/' or w[i][1]=='/' or w[i][0]=='X' or w[i][1]=='X':
                    count += 1
            if count<=2:
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

def write(row,k):
    #if((k-1)>0):
        #if row[1]==row_p[1]:
            personal_lon,personal_lat =locate(row[0])
            if personal_lon==-1 and personal_lat==-1:
                return None
            weather = find_obsv(personal_lon,personal_lat,row[1])
            #print(weather)
            return row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],weather[0],weather[1],weather[2],weather[3],weather[4],weather[5],weather[6],weather[7],weather[8],weather[9],weather[10],weather[11],weather[12],weather[13],weather[14],weather[15],weather[16],weather[17],weather[18],weather[19],weather[20],weather[21],weather[22],weather[23],row[56],row[57],row[58],row[59],row[60],row[61],row[62],row[63],row[64],row[65],row[66],row[67],row[68],row[69],row[70],row[71],row[72],row[73],row[74],row[75],row[76],row[77]
            
        #else:
        #    return None
    #else:
    #    return None

def multicore(rowlist,datalist): 
    zip_data = list(zip(rowlist,datalist))
    data = pool.starmap(write,zip_data) # 使用 pool 還可以接到 function 的回傳值
    with open("taipei.csv",'a',newline='')as csvfile:
        writer = csv.writer(csvfile)
        for m in range(len(data)):
            if data[m]!=None:
                #print(data[m])
                #cursor.execute("INSERT INTO `loss` (`PatientID`,`start-time`,`end-time`,`SP-start`,`DP-start`,`SP-end`,`DP-end`,`HR`,`temperature1`,`temperature2`,`temperature3`,`temperature4`,`temperature5`,`temperature6`,`temperature7`,`temperature8`,`temperature9`,`temperature10`,`temperature11`,`temperature12`,`temperature13`,`temperature14`,`temperature15`,`temperature16`,`temperature17`,`temperature18`,`temperature19`,`temperature20`,`temperature21`,`temperature22`,`temperature23`,`temperature24`,`humidity1`,`humidity2`,`humidity3`,`humidity4`,`humidity5`,`humidity6`,`humidity7`,`humidity8`,`humidity9`,`humidity10`,`humidity11`,`humidity12`,`humidity13`,`humidity14`,`humidity15`,`humidity16`,`humidity17`,`humidity18`,`humidity19`,`humidity20`,`humidity21`,`humidity22`,`humidity23`,`humidity24`) VALUES(%s ,%s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                writer.writerow([data[m][0],data[m][1],data[m][2],data[m][3],data[m][4],data[m][5],data[m][6],data[m][7]
                ,data[m][8][0],data[m][9][0],data[m][10][0],data[m][11][0],data[m][12][0],data[m][13][0],data[m][14][0],data[m][15][0]
                ,data[m][16][0],data[m][17][0],data[m][18][0],data[m][19][0],data[m][20][0],data[m][21][0],data[m][22][0],data[m][23][0]
                ,data[m][24][0],data[m][25][0],data[m][26][0],data[m][27][0],data[m][28][0],data[m][29][0],data[m][30][0],data[m][31][0]
                ,data[m][8][1],data[m][9][1],data[m][10][1],data[m][11][1],data[m][12][1],data[m][13][1],data[m][14][1],data[m][15][1]
                ,data[m][16][1],data[m][17][1],data[m][18][1],data[m][19][1],data[m][20][1],data[m][21][1],data[m][22][1],data[m][23][1]
                ,data[m][24][0],data[m][25][0],data[m][26][0],data[m][27][0],data[m][28][0],data[m][29][0],data[m][30][0],data[m][31][0]
                ,data[m][32],data[m][33],data[m][34],data[m][35],data[m][36],data[m][37],data[m][38],data[m][39],data[m][40]
                ,data[m][41],data[m][42],data[m][43],data[m][44],data[m][45],data[m][46],data[m][47],data[m][48],data[m][49],data[m][50],data[m][51],data[m][52],data[m][53]])
                #cursor.execute("UPDATE `temperature` SET `temperature25`=%s,`temperature26`=%s,`temperature27`=%s,`temperature28`=%s,`temperature29`=%s,`temperature30`=%s,`temperature31`=%s,`temperature32`=%s,`temperature33`=%s,`temperature34`=%s,`temperature35`=%s,`temperature36`=%s,`temperature37`=%s,`temperature38`=%s,`temperature39`=%s,`temperature40`=%s,`temperature41`=%s,`temperature42`=%s,`temperature43`=%s,`temperature44`=%s,`temperature45`=%s,`temperature46`=%s,`temperature47`=%s,`temperature48`=%s,`humidity25`=%s,`humidity26`=%s,`humidity27`=%s,`humidity28`=%s,`humidity29`=%s,`humidity30`=%s,`humidity31`=%s,`humidity32`=%s,`humidity33`=%s,`humidity34`=%s,`humidity35`=%s,`humidity36`=%s,`humidity37`=%s,`humidity38`=%s,`humidity39`=%s,`humidity40`=%s,`humidity41`=%s,`humidity42`=%s,`humidity43`=%s,`humidity44`=%s,`humidity45`=%s,`humidity46`=%s,`humidity47`=%s,`humidity48`=%s WHERE `PatientID`=%s AND `start-time`=%s",
                #(data[m][8][0],data[m][9][0],data[m][10][0],data[m][11][0],data[m][12][0],data[m][13][0],data[m][14][0],data[m][15][0]
                #,data[m][16][0],data[m][17][0],data[m][18][0],data[m][19][0],data[m][20][0],data[m][21][0],data[m][22][0],data[m][23][0]
                #,data[m][24][0],data[m][25][0],data[m][26][0],data[m][27][0],data[m][28][0],data[m][29][0],data[m][30][0],data[m][31][0]
                #,data[m][8][1],data[m][9][1],data[m][10][1],data[m][11][1],data[m][12][1],data[m][13][1],data[m][14][1],data[m][15][1]
                #,data[m][16][1],data[m][17][1],data[m][18][1],data[m][19][1],data[m][20][1],data[m][21][1],data[m][22][1],data[m][23][1]
                #,data[m][24][1],data[m][25][1],data[m][26][1],data[m][27][1],data[m][28][1],data[m][29][1],data[m][30][1],data[m][31][1],data[m][0],data[m][1]))
    csvfile.close()
    return

if __name__=='__main__':
    #time.sleep(5)
    #responce = requests.get("https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467410&stname=%25E8%2587%25BA%25E5%258D%2597&datepicker=2018-11-01",timeout=(3,7))
    pool = mp.Pool() 
    with open('2022_02_22 - 複製.csv','r',newline='',encoding='big5') as csvfile:
        Rows = csv.reader(csvfile)
        rows = list(Rows)
        for i in tqdm(range(int(len(rows)/100)+1)):
            row_plist = []
            rowlist = []
            #cursor = connection.cursor()
            if((i+1)*100<=len(rows)):
                datalist = range(i*100+1,(i+1)*100+1)
                for l in range(100):
                    rowlist.append(rows[i*100+1+l])
            else:
                datalist = range((i)*100+1,len(rows)+1)
                for l in range(len(rows)%100):
                    rowlist.append(rows[l])
            multicore(rowlist,datalist)
            #cursor.close()
            #connection.commit()
            #write(rows[i],rows[i-1],i)
    csvfile.close()   
#connection.close()

#https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467410&stname=%25E8%2587%25BA%25E5%258D%2597&datepicker=2018-11-01
#https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467420&stname=%25E6%25B0%25B8%25E5%25BA%25B7&datepicker=2018-11-01