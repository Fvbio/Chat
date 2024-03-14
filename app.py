from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('chatroom'))  # Rediriger vers la page du salon de discussion
    return render_template('home.html')

@app.route('/chatroom')
def chatroom():
    if 'username' not in session:
        return redirect(url_for('home'))
    username = session['username']
    return render_template('home.html', username=username)

@socketio.on('message')
def handleMessage(msg):
    username = session.get('username', 'Utilisateur')
    print(f'{username}: {msg}')
    send(f'{username}: {msg}', broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
