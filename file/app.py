from flask import Flask,render_template,flash, request, redirect, url_for,Response
from flask_socketio import SocketIO,send
import os
import cv2
# from server import frame1
import imagezmq
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
import json
import requests
app = Flask(__name__)
imageHub = imagezmq.ImageHub()

ALLOWED_EXTENSIONS = {'h5'}
@app.route('/')
def signin():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/autonomus')
def autonomus():
    return render_template( 'index3.html' )

@app.route('/training')
def training():
    return render_template('training.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadLabel', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save("./upload/"+filename)
            #upload file to google drive
            gfile = drive.CreateFile({'parents': [{'id': '1r0V3vOheKCTNqkXFQeN2ROfdDj8X2juZ'}]})
            gfile['title'] = "model.h5"
            gfile.SetContentFile('./upload/' + filename)
            gfile.Upload()
            gfile.content.close()
            os.remove('./upload/'+filename)
    return render_template('index3.html')

def gen_frames():
    while True:
        (rpiName, frame1) = imageHub.recv_image()
        imageHub.send_reply(b'OK')
        frame = frame1  # read the camera frame

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.event
def connect():
    print("connected")

@socketio.event
def disconnect():
    print("disconnected")

@socketio.on('message')
def handleMessage(msg):
	print(msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
