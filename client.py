# encoding: utf-8
import socket
s = socket.socket()
HOST = ''
PORT = 50007
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(b'hello')
    data = s.recv()
print('Received',repr(data))

