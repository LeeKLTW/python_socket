# encoding: utf-8
import socket

s = socket.socket()
HOST = ''
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        ping = str(input("input or exit>>"))
        if ping == 'exit':
            print('exit')
            break
        s.sendall(ping.encode())
        data = s.recv(1024)
        print('Received', repr(data))
