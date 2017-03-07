#!/usr/bin/python3
 
import socket
import re
import operator
import sys

MAXBUF = 4096
SENTINEL = 'flag'
CTF_BOT = ('ctf.crikeycon.com', 43981)


if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(CTF_BOT)

    while True:
        data = b''

        # receive and store data
        while True:
            chunk = client.recv(MAXBUF)
            data += chunk
            if len(chunk) < MAXBUF:
                break
        
        # store decoded data for future usage
        decoded = data.decode('utf-8')
        
        # print out response packet
        print(decoded)

        # our flag contains flag{}, once it's revealed print recevied data and exit
        if SENTINEL in decoded:
            break

        # skip loop until we see our X * Y = Z line
        if not re.search('[*]', decoded):
            continue

        # select integers and store into capture group
        match = re.search('(\d+)', decoded)
        
        print('Number #1: ' + match.group(0))
        print('Number #2: ' + match.group(1))
        
        expression = match.group(0)
 
        # properly handle division
        if '/' in expression:
            expression = expression.replace('/', '//')
 
        result = eval(expression)
 
        # print results to screen to see script progress
        print(expression + ' = ' + str(result))

        # encode and transfer
        data = str(result).encode('utf-8') + b'\n'
        print('Sending: ' + str(result))
        client.send(data)