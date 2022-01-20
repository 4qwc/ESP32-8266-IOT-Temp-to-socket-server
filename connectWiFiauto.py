# # ใช้กับบอร์ด ESP8266

# automaticallt connect to your WiFi
def do_connect():
    
    from machine import Pin, I2C
    import time
    import ssd1306
    import network
    
    # # OLED
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        
        oled.fill(0)
        oled.text('connecting to', 0, 16)
        oled.text('network...', 0, 28)
        oled.show()
        
        sta_if.active(True)
        sta_if.connect('iPhone', 'aaa12345')
        
        while not sta_if.isconnected():
            pass
        
    print('network config:', sta_if.ifconfig())
    
    ipaddr = sta_if.ifconfig()[0]
    oled.fill(0)
    oled.text('IP:{} '.format(ipaddr), 0, 0)
    oled.text('Connection', 0, 20)
    oled.show()
 
do_connect()
 

 
        
 
  