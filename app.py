from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, send

# Initialisation de l'application Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Emilienquipete'  # Clé secrète pour les sessions
socketio = SocketIO(app)  # Initialisation de l'extension SocketIO

# Route pour la page d'accueil
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Si le formulaire est soumis en méthode POST, enregistrer le nom d'utilisateur dans la session
        session['username'] = request.form['username']
        return redirect(url_for('chatroom'))  # Rediriger vers la page du salon de discussion
    return render_template('home.html')  # Afficher le template pour la page d'accueil

# Route pour la page du salon de discussion
@app.route('/chatroom')
def chatroom():
    if 'username' not in session:  # Vérifier si le nom d'utilisateur est enregistré dans la session
        return redirect(url_for('home'))  # Rediriger vers la page d'accueil si le nom d'utilisateur n'est pas enregistré
    username = session['username']  # Récupérer le nom d'utilisateur de la session
    return render_template('home.html', username=username)  # Afficher le template pour la page du salon de discussion

# Gestion des messages avec SocketIO
@socketio.on('message')
def handleMessage(msg):
    username = session.get('username', 'Utilisateur')  # Récupérer le nom d'utilisateur de la session, sinon utiliser "Utilisateur" par défaut
    print(f'{username}: {msg}')  # Afficher le message côté serveur
    send(f'{username}: {msg}', broadcast=True)  # Envoyer le message à tous les clients connectés

# Point d'entrée de l'application
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)  # Lancer l'application avec SocketIO sur toutes les interfaces, en mode debug
