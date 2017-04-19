import socket

s= socket.socket()

s.bind(('localhost',1234))
s.listen(5)

print('Server Started')

clientsok, clientadrss=s.accept()

val = clientsok.recv(2222)

print(val)
clientsok.send(b'Thanks from server')
s.close()