import socket

def start_server():
    host = 'localhost'
    port = 8000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print("Le serveur est prêt à recevoir des connexions...")
    
    
    while True:
        conn, addr = server.accept()
        print('Connecté à :', addr)
        while True:
            message = conn.recv(1024).decode()
            if not message:
                break
            print("De l'utilisateur :", message)
            message = input(' -> ')
            conn.send(message.encode())
        conn.close()

if __name__ == '__main__':
    start_server()
