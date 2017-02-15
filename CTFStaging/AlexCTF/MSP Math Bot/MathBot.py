#!/usr/bin/python3
 
import socket
import re
import operator

MAXBUF = 4096
SENTINEL = 'ALEXCTF'
CTF_BOT = ('195.154.53.62', 1337)
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,  # // operator
    '%': operator.mod
}

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

        # our flag contains ALEXCTF, once it's revealed print recevied data and exit
        if SENTINEL in decoded:
            print(decoded)
            break
        
        # \d+ matches a digit (equal to [0-9])
        # .{3} matches any  character, except line terminators exactly three times
        match = re.search('\d+.{3}\d+', decoded)
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
        data = str(result).encode('utf-8') + b'\n'
        client.send(data)