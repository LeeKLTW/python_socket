# encoding: utf-8
import socket

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('Server starts listening.')

while True:
    conn, addr = s.accept()
    # print('Connected by', addr)
    print(str(addr[0])+':'+str(addr[1]))

    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            conn.sendall(b'PONG' + data)
