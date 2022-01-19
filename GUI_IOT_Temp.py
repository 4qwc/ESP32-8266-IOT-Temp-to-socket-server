from tkinter import *
from tkinter import ttk

import time
import socket
import threading


from songline import Sendline
token =  'KIkEeNfW20s0geXlrqLYj5N292dHQrkal4ZM6IWo3zI'
m = Sendline(token)


serverip = '172.20.10.4' #your ip
port = 9500

def Runserver():
	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		server.bind((serverip,port))
		server.listen(5)
		print('Wating for client....')

		client, addr = server.accept()
		print('Connected from: ',addr)
		data = client.recv(1024).decode('utf-8')
		print('Message from client: ',data)
		
		v_temptext.set(data)
		#m.sendtext('{}'.format(data))

		text = 'We received your Message!'
		client.send(text.encode('utf-8'))
		client.close()

def RunserverThread():
	task1 = threading.Thread(target=Runserver)
	task1.start()

GUI = Tk()
GUI.title('TEMP FROM Micro Pythom')
GUI.geometry('600x300+200+150')

v_temptext = StringVar()
v_temptext.set('---TEMP AND HUMID---')
L1 = ttk.Label(GUI,textvariable=v_temptext,foreground='yellow',background='black',font=('Impact',40),)
L1.pack(pady=20)



RunserverThread()


GUI.mainloop()