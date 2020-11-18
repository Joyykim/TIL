import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 9999))
server_socket.listen()
client_socket, addr = server_socket.accept()

while True:
    data = client_socket.recv(4096)
    print('test')
    print(data.decode('utf-8'))
client_socket.close()
server_socket.close()
