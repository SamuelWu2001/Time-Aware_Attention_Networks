import pandas as pd  
import numpy as np
import pickle
from tqdm import tqdm
from datetime import datetime
pd.set_option('mode.chained_assignment', None)
c = pd.read_csv('2022_02_22.csv',low_memory=False)
inputs = c.fillna(-1)

dc = []
label = []
time = []
value = []
non_time = []
pre_time = []
label2 = []

temp_change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
humid_change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
train_id =[16994863, 17017635, 17029540, 17098226, 17137845, 17214318, 17368451, 17573296, 17651686, 17743754, 17934779, 18081623, 18141055, 18372425, 18495752, 18629265, 19268638, 353136, 982838, 1219081, 1959011, 2092180, 4187436, 4291399, 5697801, 6111394, 7426749, 7433719, 8220428, 8258955, 15388684, 2860783, 10459790,-1]
i=464610
id = 0
old_patient = 16994863
count = 0
j=464610 #338278 #464610
n_count = 0
pre_date_id = i-1
new_date_id = i-1
pre_date_id_2 = i-1
new_date_id_2 = i-1
firstday= ''
print(len(train_id))
while(id < 34): 
    print('id:',id,'--------------------------------------------------------------------------') 
    valid = 1
    if (len(pre_time) != len(time)): break
    #if (len(label2) != len(time)): break
    ########################################################111111111111111111111111111111
    firstday = ''
    idv = 0
    while True:
        input = inputs.iloc[i]
        pre_input = inputs.iloc[new_date_id]
        i+=1
        if(input['start-time'][0:-6] != pre_input['start-time'][0:-6]):
            new_date_id = i-1
            pre_date_id = new_date_id-1
            valid = 1
            #print('new_date_id,pre_date_id',new_date_id,pre_date_id,inputs.iloc[new_date_id]['start-time'][0:-6],inputs.iloc[pre_date_id]['start-time'][0:-6])
        
        if((pre_date_id<4) or (inputs.iloc[pre_date_id]['start-time'][0:-6]!=inputs.iloc[pre_date_id-3]['start-time'][0:-6])):
            continue
        if idv==0 : 
            print(input['PatientID'], train_id[id],old_patient)
            idv=1
        #print(i,input['PatientID'] ,train_id[id])

        if (input['PatientID'] == train_id[id] and firstday ==''):    # 新病人第一天不拿
            valid = 0
            print(input['PatientID'])
            firstday = input['start-time'][0:-6]
            print(firstday)
            continue

        if (input['PatientID'] == train_id[id] and input['start-time'][0:-6] != firstday and firstday!=''):
            valid = 1

        if valid==0: continue 
        
        if (input['PatientID'] == train_id[id-1]):
            continue
        elif (input['PatientID'] != old_patient):
            print('count = ',count)
            n_count = count
            count = 0
            firstday = ''
            break
        else:
            input_t = []
            if input['SP-end']=='None' or input['SP-end']=='-': continue
            if input['SP-start']=='None' or input['SP-start']=='-': continue

            if inputs.iloc[pre_date_id+1]['SP-end']=='None' or inputs.iloc[pre_date_id+1]['SP-end']=='-' : continue
            if inputs.iloc[pre_date_id+1]['SP-start']=='None' or inputs.iloc[pre_date_id+1]['SP-start']=='-': continue
            if inputs.iloc[pre_date_id+1]['start-weight'] == 'None' or inputs.iloc[pre_date_id+1]['start-weight'] == '-': continue
            if inputs.iloc[pre_date_id+1]['Dialysis-blood-temp'] == 'None' or inputs.iloc[pre_date_id+1]['Dialysis-blood-temp'] == '-' : continue
            if inputs.iloc[pre_date_id+1]['blood-speed'] == 'None' or inputs.iloc[pre_date_id+1]['blood-speed'] == '-'  : continue
            if inputs.iloc[pre_date_id+1]['RR'] == 'None' or inputs.iloc[pre_date_id+1]['RR'] == '-': continue
            if inputs.iloc[pre_date_id+1]['avg-temp'] == '#DIV/0!' : continue
            if inputs.iloc[pre_date_id+1]['avg-humidity'] == '#DIV/0!' : continue
            if inputs.iloc[pre_date_id+1]['HR'] == 'None' or inputs.iloc[pre_date_id+1]['HR'] == '-': continue
            if inputs.iloc[pre_date_id+1]['DP-start'] == 'None' or inputs.iloc[pre_date_id+1]['DP-start'] == '-': continue
            
            if inputs.iloc[pre_date_id+1]['UF'] == '#DIV/0!'or inputs.iloc[pre_date_id+1]['UF'] == '#VALUE!' : continue
            if inputs.iloc[pre_date_id+1]['sex'] == 'None' : continue
            if inputs.iloc[pre_date_id+1]['hypertension'] == 'None' : continue
            if inputs.iloc[pre_date_id+1]['cardiovascular'] == 'None' : continue
            if inputs.iloc[pre_date_id+1]['diabetes'] == 'None' : continue
            if inputs.iloc[pre_date_id+1]['Age'] == 'None' : continue

            if inputs.iloc[pre_date_id]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id]['RR'] == 'None' : continue

            if inputs.iloc[pre_date_id-1]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id-1]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id-1]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id-1]['RR'] == 'None' : continue

            if inputs.iloc[pre_date_id-2]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id-2]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id-2]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id-2]['RR'] == 'None' : continue

            if inputs.iloc[pre_date_id-3]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id-3]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id-3]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id-3]['RR'] == 'None' : continue
            #print(input['UF'],input['avg-temp'])

            temp_change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            humid_change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            for k in range(1,25):
                if inputs.iloc[pre_date_id+1]['temperature'+str(k)]=='X'or inputs.iloc[pre_date_id+1]['temperature'+str(k)]=='/'or inputs.iloc[pre_date_id+1]['temperature'+str(k)]=='...': temp_change[k-1] = 1
                if inputs.iloc[pre_date_id+1]['humidity'+str(k)]=='X'or inputs.iloc[pre_date_id+1]['humidity'+str(k)]=='/'or inputs.iloc[pre_date_id+1]['humidity'+str(k)]=='...': humid_change[k-1] = 1
            try :
                if ((((int(input['SP-start'])>=160) and (int(input['SP-end'])<=100)) or (int(input['SP-end'])<=90)) and (int(input['SP-end'])!=-1)):
                    #print(input['SP-start'],input['SP-end'],i,count)
                    pre_time.append([[float(inputs.iloc[pre_date_id-3]['DP-start']),float(inputs.iloc[pre_date_id-3]['SP-start']),float(inputs.iloc[pre_date_id-3]['HR']),float(inputs.iloc[pre_date_id-3]['RR'])],[float(inputs.iloc[pre_date_id-2]['DP-start']),float(inputs.iloc[pre_date_id-2]['SP-start']),float(inputs.iloc[pre_date_id-2]['HR']),float(inputs.iloc[pre_date_id-2]['RR'])],[float(inputs.iloc[pre_date_id-1]['DP-start']),float(inputs.iloc[pre_date_id-1]['SP-start']),float(inputs.iloc[pre_date_id-1]['HR']),float(inputs.iloc[pre_date_id-1]['RR'])],[float(inputs.iloc[pre_date_id]['DP-start']),float(inputs.iloc[pre_date_id]['SP-start']),float(inputs.iloc[pre_date_id]['HR']),float(inputs.iloc[pre_date_id]['RR'])]])
                    #print('i,pre_date_id',i,pre_date_id,inputs.iloc[pre_date_id+1]['start-time'])
                    #print(inputs.iloc[pre_date_id+1]['DP-start'],inputs.iloc[pre_date_id+1]['SP-start'],inputs.iloc[pre_date_id+1]['HR'],inputs.iloc[pre_date_id+1]['RR'],inputs.iloc[pre_date_id+1]['start-weight'],inputs.iloc[pre_date_id+1]['Dialysis-blood-temp'],inputs.iloc[pre_date_id+1]['blood-speed'],inputs.iloc[pre_date_id+1]['UF']
                    #,inputs.iloc[pre_date_id+1]['sex'],inputs.iloc[pre_date_id+1]['hypertension'],inputs.iloc[pre_date_id+1]['cardiovascular'],inputs.iloc[pre_date_id+1]['diabetes'],inputs.iloc[pre_date_id+1]['Age'])
                    non_time.append([float(inputs.iloc[pre_date_id+1]['DP-start']),float(inputs.iloc[pre_date_id+1]['SP-start']),float(inputs.iloc[pre_date_id+1]['HR']),float(inputs.iloc[pre_date_id+1]['RR']),float(inputs.iloc[pre_date_id+1]['start-weight']),float(inputs.iloc[pre_date_id+1]['Dialysis-blood-temp']),float(inputs.iloc[pre_date_id+1]['blood-speed']),float(inputs.iloc[pre_date_id+1]['UF'])
                    ,float(inputs.iloc[pre_date_id+1]['sex']),float(inputs.iloc[pre_date_id+1]['hypertension']),float(inputs.iloc[pre_date_id+1]['cardiovascular']),float(inputs.iloc[pre_date_id+1]['diabetes']),float(inputs.iloc[pre_date_id+1]['Age'])])  
                    #pre_time.append([[float(inputs.iloc[pre_date_id-3]['DP-start']),float(inputs.iloc[pre_date_id-3]['SP-start']),float(inputs.iloc[pre_date_id-3]['HR']),float(inputs.iloc[pre_date_id-3]['RR'])],[float(inputs.iloc[pre_date_id-2]['DP-start']),float(inputs.iloc[pre_date_id-2]['SP-start']),float(inputs.iloc[pre_date_id-2]['HR']),float(inputs.iloc[pre_date_id-2]['RR'])],[float(inputs.iloc[pre_date_id-1]['DP-start']),float(inputs.iloc[pre_date_id-1]['SP-start']),float(inputs.iloc[pre_date_id-1]['HR']),float(inputs.iloc[pre_date_id-1]['RR'])],[float(inputs.iloc[pre_date_id]['DP-start']),float(inputs.iloc[pre_date_id]['SP-start']),float(inputs.iloc[pre_date_id]['HR']),float(inputs.iloc[pre_date_id]['RR'])]])
                    #print('ok')
                    #print(temp_change)
                    #print(humid_change)
                    for k in range(1,25):
                        if temp_change[k-1]==1 and humid_change[k-1]==1:
                            input_t.append([float(inputs.iloc[pre_date_id+1]['avg-temp']),float(inputs.iloc[pre_date_id+1]['avg-humidity'])])
                        elif temp_change[k-1]==1 and humid_change[k-1]==0:
                            input_t.append([float(inputs.iloc[pre_date_id+1]['avg-temp']),float(inputs.iloc[pre_date_id+1]['humidity'+str(k)])])
                        elif temp_change[k-1]==0 and humid_change[k-1]==1:
                            input_t.append([float(inputs.iloc[pre_date_id+1]['temperature'+str(k)]),float(inputs.iloc[pre_date_id+1]['avg-humidity'])])
                        else :
                            input_t.append([float(inputs.iloc[pre_date_id+1]['temperature'+str(k)]),float(inputs.iloc[pre_date_id+1]['humidity'+str(k)])])
                    #input_t = np.array(input_t)
                    #print('i-pre_date_id',i,pre_date_id)
                    #print('ok1')
                    value.append(input_t)
                    label.append(1)  
                    t = [1440,1380,1320,1260,1200,1140,1080,1020,960,900,840,780,720,660,600,540,480,420,360,300,240,180,120,60]
                    time.append(t)
                    dc.append([[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]])
                    #print('ok2')
                    #print(input['end-time'],inputs.iloc[pre_date_id+1]['start-time'])
                    time_a = datetime.strptime(input['end-time'],'%Y/%m/%d %H:%M')
                    time_b = datetime.strptime(inputs.iloc[pre_date_id+1]['start-time'],'%Y/%m/%d %H:%M')
                    print(input['start-time'],input['end-time'])
                    delta = time_a-time_b
                    #print(int(delta.total_seconds()/60))
                    #label2.append(int(delta.total_seconds()/60))
                    count+=1
                    valid = 0
                    #print('count',count)
                    #print('i',i)
                    if (count>=5):
                        print('count = ',count)
                        n_count = count
                        count = 0
                        firstday = ''
                        break
            except:
                continue
    ############################################################000000000000000000000000000000
    #print(firstday)
    firstday = ''
    valid = 1
    while True:
        input = inputs.iloc[j]
        pre_input = inputs.iloc[new_date_id_2]
        j+=1
        if(input['start-time'][0:-6] != pre_input['start-time'][0:-6]):
            new_date_id_2 = j-1
            pre_date_id_2 = new_date_id_2-1
            valid = 1
        
        if((pre_date_id_2<4) or (inputs.iloc[pre_date_id_2]['start-time'][0:-6]!=inputs.iloc[pre_date_id_2-3]['start-time'][0:-6])):
            continue

        if (input['PatientID'] == train_id[id] and firstday==''):    # 新病人第一天不拿
            valid = 0
            firstday = input['start-time'][0:-6]
            #print(firstday)
            continue

        if (input['PatientID'] == train_id[id] and input['start-time'][0:-6] != firstday and firstday!=''):
            valid = 1

        if valid==0: continue 

        if (input['PatientID'] == train_id[id-1]):
            continue
        elif (input['PatientID'] != old_patient):
            print('count = ',count)
            old_patient = input['PatientID']
            count = 0
            id+=1
            firstday = ''
            break
        else:   
            if(n_count==0):
                print('count = ',count)
                id+=1
                old_patient = train_id[id]
                count = 0 
                break
            input_t = []
            if input['SP-end']=='None' or input['SP-end']=='-': continue
            if input['SP-start']=='None' or input['SP-start']=='-': continue

            if inputs.iloc[pre_date_id_2+1]['SP-end']=='None' or inputs.iloc[pre_date_id_2+1]['SP-end']=='-' : continue
            if inputs.iloc[pre_date_id_2+1]['SP-start']=='None' or inputs.iloc[pre_date_id_2+1]['SP-start']=='-': continue
            if inputs.iloc[pre_date_id_2+1]['start-weight'] == 'None' or inputs.iloc[pre_date_id_2+1]['start-weight'] == '-': continue
            if inputs.iloc[pre_date_id_2+1]['Dialysis-blood-temp'] == 'None' or inputs.iloc[pre_date_id_2+1]['Dialysis-blood-temp'] == '-' : continue
            if inputs.iloc[pre_date_id_2+1]['blood-speed'] == 'None' or inputs.iloc[pre_date_id_2+1]['blood-speed'] == '-'  : continue
            if inputs.iloc[pre_date_id_2+1]['RR'] == 'None' or inputs.iloc[pre_date_id_2+1]['RR'] == '-': continue
            if inputs.iloc[pre_date_id_2+1]['avg-temp'] == '#DIV/0!' : continue
            if inputs.iloc[pre_date_id_2+1]['avg-humidity'] == '#DIV/0!' : continue
            if inputs.iloc[pre_date_id_2+1]['HR'] == 'None' or inputs.iloc[pre_date_id_2+1]['HR'] == '-': continue
            if inputs.iloc[pre_date_id_2+1]['DP-start'] == 'None' or inputs.iloc[pre_date_id_2+1]['DP-start'] == '-': continue
            
            if inputs.iloc[pre_date_id_2+1]['UF'] == '#DIV/0!'or inputs.iloc[pre_date_id_2+1]['UF'] == '#VALUE!' : continue
            if inputs.iloc[pre_date_id_2+1]['sex'] == 'None' : continue
            if inputs.iloc[pre_date_id_2+1]['hypertension'] == 'None' : continue
            if inputs.iloc[pre_date_id_2+1]['cardiovascular'] == 'None' : continue
            if inputs.iloc[pre_date_id_2+1]['diabetes'] == 'None' : continue
            if inputs.iloc[pre_date_id_2+1]['Age'] == 'None' : continue

            if inputs.iloc[pre_date_id_2]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id_2]['RR'] == 'None' : continue

            if inputs.iloc[pre_date_id_2-1]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-1]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-1]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-1]['RR'] == 'None' : continue

            if inputs.iloc[pre_date_id_2-2]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-2]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-2]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-2]['RR'] == 'None' : continue

            if inputs.iloc[pre_date_id_2-3]['DP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-3]['SP-start'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-3]['HR'] == 'None' : continue
            if inputs.iloc[pre_date_id_2-3]['RR'] == 'None' : continue

            temp_change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            humid_change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            for k in range(1,25):
                if inputs.iloc[pre_date_id_2+1]['temperature'+str(k)]=='X'or inputs.iloc[pre_date_id_2+1]['temperature'+str(k)]=='/'or inputs.iloc[pre_date_id_2+1]['temperature'+str(k)]=='...': temp_change[k-1] = 1
                if inputs.iloc[pre_date_id_2+1]['humidity'+str(k)]=='X'or inputs.iloc[pre_date_id_2+1]['humidity'+str(k)]=='/'or inputs.iloc[pre_date_id_2+1]['humidity'+str(k)]=='...': humid_change[k-1] = 1
            
            try :
                if ((((int(input['SP-start'])>=160) and (int(input['SP-end'])<=100)) or (int(input['SP-end'])<=90)) and (int(input['SP-end'])!=-1)):
                    continue
                elif int(input['SP-end'])!=-1:
                    #print(input['SP-start'],input['SP-end'],j)
                    pre_time.append([[float(inputs.iloc[pre_date_id_2-3]['DP-start']),float(inputs.iloc[pre_date_id_2-3]['SP-start']),float(inputs.iloc[pre_date_id_2-3]['HR']),float(inputs.iloc[pre_date_id_2-3]['RR'])],[float(inputs.iloc[pre_date_id_2-2]['DP-start']),float(inputs.iloc[pre_date_id_2-2]['SP-start']),float(inputs.iloc[pre_date_id_2-2]['HR']),float(inputs.iloc[pre_date_id_2-2]['RR'])],[float(inputs.iloc[pre_date_id_2-1]['DP-start']),float(inputs.iloc[pre_date_id_2-1]['SP-start']),float(inputs.iloc[pre_date_id_2-1]['HR']),float(inputs.iloc[pre_date_id_2-1]['RR'])],[float(inputs.iloc[pre_date_id_2]['DP-start']),float(inputs.iloc[pre_date_id_2]['SP-start']),float(inputs.iloc[pre_date_id_2]['HR']),float(inputs.iloc[pre_date_id_2]['RR'])]])
                    #print('j,pre_date_id_2',j,pre_date_id_2,inputs.iloc[pre_date_id_2+1]['start-time'])
                    #print(inputs.iloc[pre_date_id_2+1]['DP-start'],inputs.iloc[pre_date_id_2+1]['SP-start'],inputs.iloc[pre_date_id_2+1]['HR'],inputs.iloc[pre_date_id_2+1]['RR'],inputs.iloc[pre_date_id_2+1]['start-weight'],inputs.iloc[pre_date_id_2+1]['Dialysis-blood-temp'],inputs.iloc[pre_date_id_2+1]['blood-speed'],inputs.iloc[pre_date_id_2+1]['UF']
                    #,inputs.iloc[pre_date_id_2+1]['sex'],inputs.iloc[pre_date_id_2+1]['hypertension'],inputs.iloc[pre_date_id_2+1]['cardiovascular'],inputs.iloc[pre_date_id_2+1]['diabetes'],inputs.iloc[pre_date_id_2+1]['Age'])
                    non_time.append([float(inputs.iloc[pre_date_id_2+1]['DP-start']),float(inputs.iloc[pre_date_id_2+1]['SP-start']),float(inputs.iloc[pre_date_id_2+1]['HR']),float(inputs.iloc[pre_date_id_2+1]['RR']),float(inputs.iloc[pre_date_id_2+1]['start-weight']),float(inputs.iloc[pre_date_id_2+1]['Dialysis-blood-temp']),float(inputs.iloc[pre_date_id_2+1]['blood-speed']),float(inputs.iloc[pre_date_id_2+1]['UF'])
                    ,float(inputs.iloc[pre_date_id_2+1]['sex']),float(inputs.iloc[pre_date_id_2+1]['hypertension']),float(inputs.iloc[pre_date_id_2+1]['cardiovascular']),float(inputs.iloc[pre_date_id_2+1]['diabetes']),float(inputs.iloc[pre_date_id_2+1]['Age'])])                      
                    #print('len(value)',len(value),'len(non_time)',len(non_time))
                    
                    #pre_time.append([[float(inputs.iloc[pre_date_id_2-3]['DP-start']),float(inputs.iloc[pre_date_id_2-3]['SP-start']),float(inputs.iloc[pre_date_id_2-3]['HR']),float(inputs.iloc[pre_date_id_2-3]['RR'])],[float(inputs.iloc[pre_date_id_2-2]['DP-start']),float(inputs.iloc[pre_date_id_2-2]['SP-start']),float(inputs.iloc[pre_date_id_2-2]['HR']),float(inputs.iloc[pre_date_id_2-2]['RR'])],[float(inputs.iloc[pre_date_id_2-1]['DP-start']),float(inputs.iloc[pre_date_id_2-1]['SP-start']),float(inputs.iloc[pre_date_id_2-1]['HR']),float(inputs.iloc[pre_date_id_2-1]['RR'])],[float(inputs.iloc[pre_date_id_2]['DP-start']),float(inputs.iloc[pre_date_id_2]['SP-start']),float(inputs.iloc[pre_date_id_2]['HR']),float(inputs.iloc[pre_date_id_2]['RR'])]])
                    #print('ok')
                    #print(temp_change)
                    #print(humid_change)
                    for k in range(1,25):
                        if temp_change[k-1]==1 and humid_change[k-1]==1:
                            input_t.append([float(inputs.iloc[pre_date_id_2+1]['avg-temp']),float(inputs.iloc[pre_date_id_2+1]['avg-humidity'])])
                        elif temp_change[k-1]==1 and humid_change[k-1]==0:
                            input_t.append([float(inputs.iloc[pre_date_id_2+1]['avg-temp']),float(inputs.iloc[pre_date_id_2+1]['humidity'+str(k)])])
                        elif temp_change[k-1]==0 and humid_change[k-1]==1:
                            input_t.append([float(inputs.iloc[pre_date_id_2+1]['temperature'+str(k)]),float(inputs.iloc[pre_date_id_2+1]['avg-humidity'])])
                        else :
                            input_t.append([float(inputs.iloc[pre_date_id_2+1]['temperature'+str(k)]),float(inputs.iloc[pre_date_id_2+1]['humidity'+str(k)])])

                    #print('ok1')
                    input_t = np.array(input_t)
                    value.append(input_t)
                    label.append(0)
                    t = [1440,1380,1320,1260,1200,1140,1080,1020,960,900,840,780,720,660,600,540,480,420,360,300,240,180,120,60]
                    time.append(t)
                    dc.append([[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2],[1,2]])
                    #print('ok2')
                    #label2.append(0)
                    print(input['start-time'],input['end-time'])
                    count+=1
                    valid = 0
                    #print(count)
                    if count >= n_count :
                        print('count = ',count)
                        id+=1
                        old_patient = train_id[id]
                        count = 0 
                        firstday = ''
                        break
            except:
                continue

#E D H BG BK BI BH CC BV BW BX BY BZ

print('len(dc)',len(dc))
print('len(label)',len(label))
print('len(time)',len(time))
print('len(value)',len(value))
print('len(non_time)',len(non_time))
print('len(pre_time)',len(pre_time))
# print('len(label2)',len(label2))
#print(value[0])

traindata = []
traindata.append(dc[0:500000])
traindata.append(label[0:500000])
traindata.append(time[0:500000])
traindata.append(value[0:500000])
traindata.append(non_time[0:500000])
traindata.append(pre_time[0:500000])
# traindata.append(label2[0:5000])

f = open('valid_file_1_5.pickle','wb')
pickle.dump(traindata,f)
