import network
import machine

station = network.WLAN(network.STA_IF)
if station.isconnected() == True:
    print("Already connected")
station.active(True)
station.connect("<wifi id>", "<wifi password>")
while station.isconnected() == False:
    pass
print("Connection successful")
print(station.ifconfig())

import socket
from machine import Pin

led = Pin(2, Pin.OUT)

def handle_request(conn):
    data = conn.recv(1024).decode('utf-8').strip()
    print(data)
    if data == '1':
        print('Turning on LED')
        led.value(1)
    elif data == '2':
        print('Turning off LED')
        led.value(0)
    else:
        print('Unknown command:', data)

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
    server = socket.socket()
    server.bind(addr)
    server.listen(1)
    print('Listening on', addr)
    while True:
        conn, addr = server.accept()
        print('Connected by', addr)
        handle_request(conn)
        conn.close()

start_server()
