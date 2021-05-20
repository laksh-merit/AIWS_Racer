from flask import request
from flask import jsonify
from flask import Flask
import cv2
import csv
import random
import numpy as np
import os
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('video.html')
def cssv():
    APP_FOLDER = 'D:/part/'
    totalFiles = 0
    for base, dirs, files in os.walk(APP_FOLDER):
        for Files in files:
            totalFiles += 1
    output_file = open(r'D:\Flask\Image.csv', 'w', newline='')
    wr = csv.writer(output_file)
    count=0
    v=[]
    for j in range(totalFiles):
        d=r'D:/part/'+str(j)+'.jpg'
        v.append([d])
        f=random.randint(1,100)
        v[count].append(f)
        count+=1
    wr.writerows(v)
@app.route('/func',methods=['GET','POST'])
def func():
    message=request.get_json(force=True)
    n=message['frame_no']
    m=message['flag']
    a=float(n)
    cap = cv2.VideoCapture('D:/Flask/Welcome.mp4')
    last=cap.get(cv2.CAP_PROP_FRAME_COUNT)
    i=0
    while(a<=last):
        if m=='False':
            cap.set(1,a)
            ret, frame = cap.read()
            cv2.imwrite('D:/part/'+str(i)+'.jpg',frame)
            a+=1
            i+=1
            cssv();
    save="done"
    response = {
    'save': {
        'Successfull':print("captured")}
        }
    return jsonify(response)


   
