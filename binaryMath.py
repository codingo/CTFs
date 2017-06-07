import socket
import binascii
import re

RHOST = 'pwn.bne.sectalks.org'
RPORT = 10101

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

while True:
    data = s.recv(1024).decode('utf-8')
    print(data)
    data = data[12:][:-5]
    print(data)
    match = re.search('(\d+)\s.\s(\d+)', data)
    d1 = int(match.group(1), 2)
    print(d1)
    d2 = int(match.group(2), 2)
    print(d2)
    s.send(("{0:b}".format((d1+d2))).encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print(data)
