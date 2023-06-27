import socket

def send_command(cmd):
    addr = socket.getaddrinfo('<ip address>', 8080)[0][-1]
    client = socket.socket()
    client.connect(addr)
    client.send(str(cmd).encode('utf-8'))
    client.close()

while True:
    cmd = int(input('Enter command (1=on, 2=off): '))
    send_command(cmd)
