# ใช้กับบอร์ด ESP8266
from machine import Pin, I2C
import time
import dht
import ssd1306

######## set network
import socket
import network
time.sleep(3)

serverip = '172.20.10.5' #your ip
port = 9500

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
#scan_ip = sta_if.scan()
#ipaddr = sta_if.ifconfig()[0]
#print('IP: ',ipaddr)

sta_if.connect("iPhone", "aaa12345")
time.sleep(3)

network_status = sta_if.isconnected()
time.sleep(3)
print("STATUS:",sta_if.isconnected())
 #sta_if.ifconfig()

###########

# Initailize
RLPIN = 2 # Relay pin
relay = Pin(RLPIN, Pin.OUT)

# ESP32 Pin assignment 
#i2c = I2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

#oled.text('Hello, World 1!', 0, 0)
#oled.show()

#setup start ON/OFF
ON = 0
OFF = 1

def turn_on():
    relay.value(ON)
    print("RELAY ON")
    
def turn_off():
    relay.value(OFF)
    print("RELAY OFF")

# DHT22
d = dht.DHT22(Pin(2))

# conect ip index[0]
ipaddr = sta_if.ifconfig()[0]



time.sleep(2)
oled.fill(0) # clear LCD
oled.text('IP:{}'.format(ipaddr), 0, 0)
oled.show()

time.sleep(2)
oled.fill(0) # clear LCD
oled.text('Loading...', 0, 0)
oled.show()


state = False
count = 0

while True:       
    d.measure()
    temp = d.temperature()
    humid = d.humidity()
    time.sleep(5)
    
    oled.fill(0) # clear LCD
    #oled.text("wifi:{}".format(network_status), 0, 0)
    oled.text('IP:{} '.format(ipaddr), 0, 0)
    oled.text('TEMP: {} .C'.format(temp), 0, 18)
    oled.text('HUMID: {}% RH'.format(humid), 0, 40)
    oled.show()
    time.sleep(5)
    
    # ส่งค่าขึ้น sever
    data = 'TEMP: {} °C \n HUMID: {} % RH'.format(temp,humid)
    
    if network_status == True:
        textok = 'CONNECTTED'
        oled.fill(0)
        oled.text("IP: {}".format(textok) , 0, 0)
        oled.text('TEMP: {} .C'.format(temp), 0, 18)
        oled.text('HUMID: {}% RH'.format(humid), 0, 40)
        oled.show()
        
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

        server.connect((serverip,port))
        server.send(data.encode('utf-8'))

        data_server = server.recv(1024).decode('utf-8')
        print('Data from Server: ', data_server)
        server.close()
        
    else:
        textok = 'FAILED'
        oled.fill(0)
        oled.text("IP: {}".format(textok) , 0, 0)
          
        #print('TEMP {}°C / HUMID {}% RH'.format(temp,humid))
        #print('----------')
    
    
    #เช็คเงื่อนไขอุณหภูมิ
''' if temp > 30:
        state = True
        #print('TURN ON')
    else:
        state = False
        #print('TURN OFF')
        
    # ส่วนสั่งให้รีเลย์ทำงาน    
    if state == True: # ถ้าอุณภูมิ 45 c
        turn_on()     # เปิดรีเลย์
    else:
        turn_off() # ปิดรีเลย์
    #print('RELAY STATE: ', relay.value())
    print('----------')
    #count += 1 # count = count +1
    #time.sleep(3)
'''     
