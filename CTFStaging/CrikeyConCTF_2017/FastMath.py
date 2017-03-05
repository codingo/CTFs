#!/usr/bin/python3
 
import socket
import re
import operator


MAXBUF = 4096
SENTINEL = 'flag'
CTF_BOT = ('crikeyconctf.dook.biz', 23776)

last_answer='00000000000000000'

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
        
        #temporary
        print(decoded)
        #

        if last_answer in decoded:
            continue;

        # our flag contains flag{}, once it's revealed print recevied data and exit
        if SENTINEL in decoded:
            print(decoded)
            break

        match = re.search('[^\:\s]\d+.{3}\d+', decoded)

        if not match:
            raise ValueError("Invalid expression string")
        
        expression = match.group(0)
 
        # properly handle division
        if '/' in expression:
            expression = expression.replace('/', '//')
 
        result = eval(expression)
 
        # print results to screen to see script progress
        print(expression + ' = ' + str(result))

        # encode and transfer
        last_answer = str(result)
        data = str(result).encode('utf-8') + b'\n'
        print('Sending: ' + str(result))
        client.send(data)