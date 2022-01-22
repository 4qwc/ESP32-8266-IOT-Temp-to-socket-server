# ใช้กับบอร์ด ESP8266
from machine import Pin, I2C
import time

######## set network
import socket
import network
time.sleep(3)


 # automaticallt connect to your WiFi   
sta_if = network.WLAN(network.STA_IF)
def Connectauto():
    if not sta_if.isconnected():
        print('connecting to network...')
        
        network_status = sta_if.active(True)
        sta_if.connect('iPhone', 'aaa12345')
            
        while not sta_if.isconnected():
            pass
           
    print('network config:', sta_if.ifconfig()[0])
     


Connectauto()

def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
#http_get('http://micropython.org/ks/test.html')
    


serverip = '172.20.10.4' #your ip
port = 9500

pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

addr = socket.getaddrinfo(serverip, port)[0][-1]

# s = socket.socket()
# s.bind(addr)
# s.listen(1)

print('listening on', addr)

while True:
    time.sleep(2)
#     cl, addr = s.accept()
#     print('client connected from', addr)
#     cl_file = cl.makefile('rwb', 0)
#     
#     
#     while True:
#         line = cl_file.readline()
#         if not line or line == b'\r\n':
#             break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    
    cl = socket.socket()
    cl.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    
    cl.connect((serverip,port))
    cl.send(response.encode('utf-8'))
    
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    
    data_server = cl.recv(1024).decode('utf-8')
    print('Data from Server: ', data_server)
    cl.close()
    
 
 
    