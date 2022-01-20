# server.py

import socket

serverip = '172.20.10.5' #your ip for macbook
port = 9500

while True:
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	server.bind((serverip,port))
	server.listen(1)

	print('Wating for client....')
	client, addr = server.accept() #accept connection from client
	print('Connected from: ',addr)

	data = client.recv(1024).decode('utf-8')
	print('Message from client: ',data)

	text = 'Server recieved your data'
	client.send(text.encode('utf-8'))
	#client.close()