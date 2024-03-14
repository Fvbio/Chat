import socket

def start_client():
    
    host = 'localhost'
    port = 8000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    while True:
        message = input(" -> ")
        client.send(message.encode())
        data = client.recv(1024).decode()
        print('Reçu du serveur :', data)

if __name__ == '__main__':
    start_client()
