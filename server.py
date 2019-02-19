# encoding: utf-8
import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    sock, addr = s.accept()
    print('Address',addr)
    s.send(b'Welcome!')
    sock.close()
