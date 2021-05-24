import socketio
sio = socketio.Client()

@sio.event
def connect():
    print('Connection Established...')

@sio.event
def disconnect():
    print('Disconnected...')

@sio.on('message')
def handleMessage(msg):
	print(msg)

sio.connect("http://localhost:5000")
