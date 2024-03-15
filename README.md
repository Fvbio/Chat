Documentation du projet : Logiciel de chat en réseau

Objectif du projet
Le but de ce projet était de créer un logiciel de chat en Python permettant à deux personnes ou plus de communiquer en temps réel. Les communications devaient être bidirectionnelles et le délai entre l’envoi et la réception d’un message devait être négligeable.

Partie 1 - Interface en ligne de commande
Dans cette partie, nous avons créé une interface en ligne de commande simple permettant à deux utilisateurs de communiquer. Les utilisateurs peuvent saisir un message et l’envoyer, ainsi que recevoir les messages envoyés par l’autre utilisateur. Pour cela, nous avons utilisé la librairie socket.

Client                         Serveur
  |                              |
  |--- Connexion --------------->|
  |                              |
  |<-- Attente de message -------|
  |                              |
  |--- Envoi de message -------->|
  |                              |
  |<-- Réception de message -----|
  |                              |
  |--- Envoi de message -------->|
  |                              |
  |<-- Réception de message -----|
  |                              |
  |--- Déconnexion ------------->|
  |                              |

Voici comment cela fonctionne :

1. Le client établit une connexion avec le serveur.
2. Le serveur attend qu'un message soit envoyé par le client.
3. Le client envoie un message au serveur.
4. Le serveur reçoit le message et attend le prochain message.
5. Le client envoie un autre message au serveur.
6. Le serveur reçoit le message et attend le prochain message.
7. Le client se déconnecte.

C'est un cycle continu d'envoi et de réception de messages jusqu'à ce que le client se déconnecte.


Partie 2 - Chat multi-utilisateur avec interface graphique
Nous avons ensuite amélioré notre logiciel en ajoutant la possibilité pour plusieurs utilisateurs de communiquer dans un groupe et en introduisant une interface graphique. Pour cela, nous avons mis en place un serveur Flask qui fait l’intermédiaire entre les différents clients. Les interfaces graphiques ont été réalisées avec HTML, CSS et JavaScript, et sont fournies par le serveur Flask. Nous avons utilisé la librairie Flask-SocketIO pour permettre une communication bidirectionnelle entre le serveur web et le navigateur.

Client 1                        Serveur                        Client 2
  |                              |                              |
  |--- Connexion --------------->|                              |
  |                              |<-- Attente de message -------|
  |                              |                              |
  |--- Envoi de message -------->|                              |
  |                              |--- Transmission du message ->|
  |                              |<-- Réception de message -----|
  |<-- Réception de message -----|                              |
  |                              |                              |
  |--- Envoi de message -------->|                              |
  |                              |--- Transmission du message ->|
  |                              |<-- Réception de message -----|
  |<-- Réception de message -----|                              |
  |                              |                              |
  |--- Déconnexion ------------->|                              |
  |                              |                              |

1. Le Client 1 établit une connexion avec le Serveur.
2. Le Serveur attend qu'un message soit envoyé par le Client 1.
3. Le Client 1 envoie un message au Serveur.
4. Le Serveur transmet le message du Client 1 au Client 2.
5. Le Client 2 reçoit le message transmis par le Serveur. Il peut effectuer des actions en réponse au message.
6. Le Serveur reçoit un autre message du Client 1 et le transmet au Client 2. Le Client 2 peut réagir en conséquence.
7. Le Client 1 se déconnecte du Serveur. La connexion est fermée.

Dans ce schéma, le serveur agit comme un intermédiaire entre les clients. Lorsqu’un client envoie un message, le serveur le reçoit et le transmet à tous les autres clients connectés. De cette façon, tous les clients peuvent communiquer entre eux en temps réel.


Explication des fichiers:

client.py : Ce fichier contient le code pour un client de chat en réseau. Il utilise la bibliothèque socket pour établir une connexion avec un serveur et envoyer/recevoir des messages.

server.py : Ce fichier contient le code pour un serveur de chat en réseau. Il utilise également la bibliothèque socket pour accepter les connexions des clients et transmettre les messages entre eux.

home.html : Ce fichier est une page web qui fournit une interface utilisateur pour le chat. Il utilise JavaScript et la bibliothèque Socket.IO pour communiquer en temps réel avec le serveur de chat.

app.py : Ce fichier est le point d’entrée principal de l’application. Il utilise le framework Flask pour servir la page web aux clients et gérer les connexions Socket.IO. Il gère également les sessions utilisateurs pour garder une trace des noms d’utilisateurs.