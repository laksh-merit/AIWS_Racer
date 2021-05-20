import socketio
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './templates/'
})

@sio.event
def connect(sid,environ):
    print(sid,"connected")

@sio.event
def disconnect(sid):
    print(sid,"disconnected")


def message_handler(sid,msg):
    sio.send(msg)
    print(msg)
sio.on('message', message_handler)




