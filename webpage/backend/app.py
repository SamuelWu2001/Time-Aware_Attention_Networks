from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from config import Config
import mysql.connector
import sys
import json
import torch
from model import TransformerTime 
import requests
from bs4 import BeautifulSoup
from tool import find_obsv
from concurrent.futures import Executor, ThreadPoolExecutor
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle
import os
import copy
# from flask_socketio import SocketIO,emit

app = Flask(__name__,
            static_folder = "./dist/assets",
            template_folder = "./dist") 
app.config.from_object(Config)
connection = mysql.connector.connect(host='127.0.0.1',
                                    port='3306',
                                    user='root',
                                    password='2001513SamuelWu11',
                                    database='ihproject'
                                    )
cursor = connection.cursor()
cursor.execute("SET SQL_SAFE_UPDATES=0")
# socketio = SocketIO()
# socketio.init_app(app,cross_allowed_origins="*")
name_space = '/predict'
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
executor = ThreadPoolExecutor(1)
file  = open("train_file.pickle","rb")
flist = pickle.load(file)
file.close()
train_data = flist[4]
train_data = np.array(train_data)
scaler = StandardScaler(copy=True,with_mean=True,with_std=True).fit(train_data)

PatientList=[
        {
            'PatientID':'65535',
            'Name': '王O明',
            'Age':'64',
            'Sex':'1',
            'Address':'台南市永康區復國一路6巷72號',
            'hypertension': '1',
            'cardiovascular': '1',
            'diabetes': '0',
        },
        {
            'PatientID':'1072980',
            'Name': '陳O美',
            'Age':'48',
            'Sex':'0',
            'Address':'台南市南區中華路108號',
            'hypertension': '1',
            'cardiovascular': '1',
            'diabetes': '0',
        },
        {
            'PatientID':'2170850',
            'Name': '楊O龍',
            'Age': '62',
            'Sex':'1',
            'Address':'台南市永康區民族路87號',
            'hypertension': '0',
            'cardiovascular': '1',
            'diabetes': '1',
        },
    ]
HistoryList=[
      {
        'PatientID':'65535',
        'BedID':'A1' ,
        'Date': '2022/05/01',
        'one' :{
            'time' : '08:16',
            'predict' : False,
            'correct' : True,
            'SP' : 98,
            'DP' : 161,
            'HR' : 99,
            'RR' : 20
        },
        'two' :{
            'time' : '09:23',
            'predict' : False,
            'correct' : False,
            'SP' : 103,
            'DP' : 166,
            'HR' : 81,
            'RR' : 20
        },
        'three' :{
            'time' : '10:27',
            'predict' : True,
            'correct' : True,
            'SP' : 87,
            'DP' : 166,
            'HR' : 81,
            'RR' : 20
        },
        'four' :{
            'time' : '11:20',
            'predict' : False,
            'correct' : True,
            'SP' : 82,
            'DP' : 168,
            'HR' : 82,
            'RR' : 20
        },
        'five' :{
            'time' : '12:06',
            'SP' : 91,
            'DP' : 158,
            'HR' : 80,
            'RR' : 20
        },
      },
      {
        'PatientID':'123456',
        'BedID':'A2' ,
        'Date': '2022/05/01',
        'one' :{
            'time' : '09:16',
            'predict' : False,
            'correct' : True,
            'SP' : 92,
            'DP' : 166,
            'HR' : 72,
            'RR' : 18
        },
        'two' :{
            'time' : '10:47',
            'predict' : True,
            'correct' : True,
            'SP' : 100,
            'DP' : 154,
            'HR' : 72,
            'RR' : 16
        },
        'three' :{
            'time' : '11:25',
            'predict' : True,
            'correct' : False,
            'SP' : 88,
            'DP' : 164,
            'HR' : 70,
            'RR' : 20
        },
        'four' :{
            'time' : '12:20',
            'predict' : False,
            'correct' : True,
            'SP' : 98,
            'DP' : 190,
            'HR' : 68,
            'RR' : 20
        },
        'five' :{
            'time': '13:26',
            'SP': 105,
            'DP' : 184,
            'HR' : 69,
            'RR' : 17
        },
      },
      {
        'PatientID':'987654',
        'BedID':'A3' ,
        'Date': '2022/05/01',
        'one' :{
            'time' : '08:45',
            'predict' : False,
            'correct' : True,
            'SP' : 110,
            'DP' : 158,
            'HR' : 69,
            'RR' : 15
        },
        'two' :{
            'time' : '09:37',
            'predict' : False,
            'correct' : True,
            'SP' : 112,
            'DP' : 151,
            'HR' : 63,
            'RR' : 14
        },
        'three' :{
            'time' : '10:58',
            'predict' : False,
            'correct' : True,
            'SP' : 111,
            'DP' : 144,
            'HR' : 70,
            'RR' : 15
        },
        'four' :{
            'time' : '11:40',
            'predict' : False,
            'correct' : True,
            'SP' : 98,
            'DP' : 137,
            'HR' : 69,
            'RR' : 18
        },
        'five' :{
            'time': '12:26',
            'SP': 95,
            'DP' : 154,
            'HR' : 70,
            'RR' : 18
        }
      },
      {
        'PatientID':'134679',
        'BedID':'A4' ,
        'Date': '2022/05/01',
        'one' :{
            'time' : '09:16',
            'predict' : False,
            'correct' : False,
            'SP' : 95,
            'DP' : 151,
            'HR' : 84,
            'RR' : 16
        },
        'two' :{
            'time' : '10:33',
            'predict' : True,
            'correct' : True,
            'SP' : 85,
            'DP' : 147,
            'HR' : 76,
            'RR' : 20
        },
        'three' :{
            'time' : '11:56',
            'predict' : True,
            'correct' : True,
            'SP' : 86,
            'DP' : 122,
            'HR' : 90,
            'RR' : 20
        },
        'four' :{
            'time' : '12:43',
            'predict' : False,
            'correct' : True,
            'SP' : 82,
            'DP' : 127,
            'HR' : 84,
            'RR' : 16
        },
        'five' :{   
            'time': '13:28',
            'SP': 105,
            'DP' : 133,
            'HR' : 82,
            'RR' : 20
        }
      },
    ]
Positive={
    'PatientID' : '65535',
    'DP' : 60,
    'SP' : 96,
    'HR' : 136,
    'RR' : 14,
    'weight' : 51.8,
    'BT' : 36,
    'BR' : 150,
    'UF' : -4.604051565,
    'date' : '2020/8/18',
    'time' : '10:24',
    'pretime' : [[58.0, 119.0, 123.0, 20.0], [71.0, 123.0, 132.0, 16.0], [69.0, 113.0, 123.0, 20.0], [71.0, 121.0, 133.0, 17.0]],
}
Negative={
    'PatientID' : '65535',
    'DP' : 89,
    'SP' : 148,
    'HR' : 70,
    'RR' : 18,
    'weight' : 56.3,
    'BT' : 36,
    'BR' : 320,
    'UF' : 1.992753623, 
    'date' : '2016/1/14',
    'time' : '13:04',
    'pretime' : [[55.0, 110.0, 73.0, 20.0], [79.0, 127.0, 77.0, 20.0], [84.0, 132.0, 67.0, 20.0], [84.0, 152.0, 76.0, 20.0]],
}

nontime=[]
pretime=[]
temp_value=[]
model = TransformerTime()
result = []
timeseq = [[1440, 1380, 1320, 1260, 1200, 1140, 1080, 1020, 960, 900, 840, 780, 720, 660, 600, 540, 480, 420, 360, 300, 240, 180, 120, 60]]

model.load_state_dict(torch.load("./model_weight.pth",map_location=torch.device('cpu')))
model.eval()

def getkey(pid):
    for i in range(len(PatientList)):
        if PatientList[i]['PatientID']==pid:
            return i
    return -1

def predict(pdata,index):
    print(pdata)
    nontime=[]
    temp_value=[]
    print("PatientList")
    nontime.append(pdata['DP'])
    nontime.append(pdata['SP'])
    nontime.append(pdata['HR'])
    nontime.append(pdata['RR'])
    nontime.append(pdata['weight'])
    nontime.append(pdata['BT'])
    nontime.append(pdata['BR'])
    nontime.append(pdata['UF'])
    nontime.append(PatientList[index]['Sex'])
    nontime.append(PatientList[index]['hypertension'])
    nontime.append(PatientList[index]['cardiovascular'])
    nontime.append(PatientList[index]['diabetes'])
    nontime.append(PatientList[index]['Age'])
    nontime = list(map(int,nontime))
    print('nontime',nontime)
    nontime = [nontime]
    nontime = scaler.transform(nontime)
    nontime = nontime[0]
    print('nontime',nontime)
    pretime = [pdata['pretime']]
    address = PatientList[index]['Address']
    response = requests.get("https://www.google.com/maps/place?q=" + address)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.prettify()
    init = text.find("window.APP_INITIALIZATION_STATE")
    data = text[init+35:init+89]  #將其後的參數進行存取
    print(data)
    loc = data.split(',')
    #if len(loc)>=3:
    longitude = float(loc[1])
    latitude = float(loc[2])
    print(pdata['date'],pdata['time'])
    temp_value = find_obsv(longitude,latitude,pdata['date']+' '+pdata['time'])
    # temp_value = [temp_value]
    print(temp_value)
    global result
    result = model(temp_value,nontime,pretime,timeseq)
    result = result.tolist()
    print(result)
    print(result[0],result[1])
    return 

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/getdata',methods=['GET'])
def GetHistoryData():
    h = copy.deepcopy(HistoryList)
    for i in range(len(h)):
        h[i]['PatientID'] = h[i]['PatientID'] + '**'
    return jsonify(h)

@app.route('/api/getPatient',methods=['GET'])
def GetPatientData():
    p = copy.deepcopy(PatientList)
    for i in range(len(p)):
        p[i]['PatientID'] = p[i]['PatientID'] + '**'
    return jsonify(p)

@app.route('/api/download',methods=['GET'])
def Download():
    if request.args.get("file")=='1':
        return jsonify(Positive)
    if request.args.get("file")=='0':
        return jsonify(Negative)

@app.route('/api/adddata',methods=['POST'])
def AddPatientData():
    data = request.get_data()
    data = json.loads(data)
    print(data)
    PatientList.append(data)
    # cursor.execute("INSERT INTO patientlist VALUES(%s , %s, %s, %s, %s, %s, %s, %s);",(data["PatientID"],data['Name'],data['Age'],data['Sex'],data['Address'],data['hypertension'],data['cardiovascular'],data['diabetes']))  
    return 'ok'

@app.route('/api/predictdata',methods=['POST'])
def PredictData():
    file = request.files["json"]
    base_path = os.path.abspath(os.path.dirname(__file__))
    print(base_path)
    file.save(os.path.join(base_path,'upload.json'))
    with open(os.path.join(base_path,'upload.json'),'r') as f:
        data = json.load(f)
    print(data)
    index = getkey(data["PatientID"])
    if index==-1 :
        return 'error'
    executor.submit(predict,data,index)
    return 'ok'

@app.route('/api/getresult',methods=['GET'])
def GetResult():
    print(result)
    if result[1]>result[0]:
        return 'true'
    return 'false'
    

if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app, debug=True)