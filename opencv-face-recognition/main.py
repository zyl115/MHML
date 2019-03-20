ip = 'http://146.169.161.84:65080'

sio = socketio.Client()

@sio.on('connect')
def on_connect():
   print('connection established')

@sio.on('?????')
def on_message(data):
   xxxxxxxxxxx
   sio.emit('yyyyyyy', lbolean?????)

@sio.on('disconnect')
def on_disconnect():
   print('disconnected from server')

sio.connect(ip)
sio.wait()