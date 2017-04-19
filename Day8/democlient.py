import socket

s= socket.socket()

s.connect(('localhost', 1234))

s.send(b'Hello server, this is client message')

val=s.recv(2222)
print(str(val))

s.close()