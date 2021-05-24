import cv2
import os
import random
import csv
import socketio
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './templates/',
    '/assets/css/style.css':'./assets/css/style.css',
    '/static/Welcome.mp4':'./static/Welcome.mp4',
    '/assets/js/script.js' : './assets/js/script.js',
    '/assets/vendor/icofont/demo.html' : './assets/vendor/icofont/demo.html',
    '/assets/vendor/icofont/icofont.css' : './assets/vendor/icofont/icofont.css',
    '/assets/vendor/icofont/icofont.min.css' : './assets/vendor/icofont/icofont.min.css',
    '/assets/vendor/icofont/fonts/' : './assets/vendor/icofont/fonts/'

})
@sio.event
def connect(sid,environ):
    print(sid,"connected")

@sio.event
def disconnect(sid):
    print(sid,"disconnected")

def message_handler(sid,msg):
    print(msg)
    sio.send(msg)
sio.on('message', message_handler)




