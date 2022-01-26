# ใช้กับบอร์ด ESP8266
from machine import Pin, I2C
import time
import dht
import ssd1306
 

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
 

# ESP32 Pin assignment 
#i2c = I2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
 
# DHT22
d = dht.DHT22(Pin(2))

while True:       
    d.measure()
    temp = d.temperature()
    humid = d.humidity()
    time.sleep(3)
 
    print('TEMP {} HUMID {}'.format(temp, humid))
    #---- OLED ---
    oled.fill(0)
 
    oled.text('TEMP: {} .C'.format(temp), 0, 18)
    oled.text('HUMID: {}% RH'.format(humid), 0, 40)
    oled.show()
 #--------------------------
 
    
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
