import socket
import time

HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
data = 'Hello Data!'
client_socket.sendall(data.encode())
time.sleep(10)
client_socket.close()
