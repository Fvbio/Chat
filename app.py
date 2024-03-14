from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flask_socketio import join_room, leave_room

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('home.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
    
@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    send('Un utilisateur a rejoint le salon ' + room, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    send('Un utilisateur a quitté le salon ' + room, room=room)
    
if __name__ == '__main__':
    socketio.run(app, debug=True)