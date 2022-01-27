ssid = 'iPhone'
password = 'aaa12345'

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('กรุณาเชื่อมต่ออีกครั้ง...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        pass
    print('เครือข่าย IP:', sta_if.ifconfig())
    
do_connect()