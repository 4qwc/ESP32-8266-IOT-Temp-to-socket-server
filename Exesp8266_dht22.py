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

# sta_if = network.WLAN(network.STA_IF)
# sta_if.active(True)
 

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    
 # automaticallt connect to your WiFi   
sta_if = network.WLAN(network.STA_IF)

def Connectauto(str):
    if not sta_if.isconnected():
        print('connecting to network...')
            
        oled.fill(0)
        oled.text('connecting to', 0, 16)
        oled.text('network...', 0, 28)
        oled.show()
            
        network_status = sta_if.active(True)
        sta_if.connect('iPhone', 'aaa12345')
         
            
        while not sta_if.isconnected():
            pass
           
    print('network config:', sta_if.ifconfig()[0])
    return network_status   

ipaddr = sta_if.ifconfig()[0]
oled.fill(0)
oled.text('IP:{} '.format(ipaddr), 0, 0)
oled.text('Connection', 0, 20)
oled.show()


###########

# ESP32 Pin assignment 
#i2c = I2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
 
# DHT22
d = dht.DHT22(Pin(2))



#print(network_connect)
while True:       
    d.measure()
    temp = d.temperature()
    humid = d.humidity()
    time.sleep(3)
    
    oled.fill(0) # clear LCD
    #oled.text("wifi:{}".format(network_status), 0, 0)
    #oled.text('IP:{} '.format(ipaddr), 0, 0)
    oled.text('TEMP: {} .C'.format(temp), 0, 18)
    oled.text('HUMID: {}% RH'.format(humid), 0, 40)
    oled.show()
    time.sleep(3)
    
    
    
    # ส่งค่าขึ้น sever
    
    
    #if network_connect == True:
    textok = 'CONNECTTED'
    
    #---- OLED ---
    oled.fill(0)
    oled.text("IP: {}".format(textok) , 0, 0)
    oled.text('TEMP: {} .C'.format(temp), 0, 18)
    oled.text('HUMID: {}% RH'.format(humid), 0, 40)
    oled.show()
 #--------------------------
    
    # server
    
    data = 'TEMP: {} °C \n HUMID: {} % RH'.format(temp,humid)
    
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    
     
    data_server = server.recv(1024).decode('utf-8')
    print('Data from Server: ', data_server)
    server.close()    
  
    
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
