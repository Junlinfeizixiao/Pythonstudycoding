import socket

#TCP

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("127.0.0.1",9999))
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Tom',b'Anna',b'Jerry']:
# 	s.send(data)
# 	print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Tom',b'Anna',b'Jerry']:
	s.sendto(data,('127.0.0.1',9999))
	print(s.recv(1024).decode('utf-8'))
s.close()