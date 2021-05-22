import cv2
import os
import random
import csv
import socketio
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './templates/',
    '/static/steering.png':'./static/steering.png',
    '/static/Welcome.mp4':'./static/Welcome.mp4'
})

@sio.event
def connect(sid,environ):
    print(sid,"connected")

@sio.event
def disconnect(sid):
    print(sid,"disconnected")

def cssv():
    APP_FOLDER = 'part/'
    totalFiles = 0
    for base, dirs, files in os.walk(APP_FOLDER):
        for Files in files:
            totalFiles += 1
    output_file = open(r'Image.csv', 'w', newline='')
    wr = csv.writer(output_file)
    count=0
    v=[]
    for j in range(totalFiles):
        d='C:/Users/robot/Full_task/part/'+str(j)+'.jpg'
        v.append([d])
        f=random.randint(1,100)
        v[count].append(f)
        count+=1
    wr.writerows(v)



def message_handler(sid,msg):
    if msg['a'] == 'False':
        sio.send(msg['val'])
        print(msg['val'])
    else:
        n = msg['frame_no']
        m = msg['flag']
        a = float(n)
        cap = cv2.VideoCapture('static/Welcome.mp4')
        last = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        i = 0
        while (a <= last):
            if m == 'False':
                cap.set( 1, a )
                ret, frame = cap.read()
                cv2.imwrite('part/' + str(i) + '.jpg', frame)
                a += 1
                i += 1
                cssv();

sio.on('message', message_handler)




