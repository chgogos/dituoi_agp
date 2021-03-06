# server-1.py
from socket import *
from fib import fib 

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client,addr = sock.accept()  # waits for a connection to be established
        print("Connection", addr)
        fib_handler(client) # passes the client to a handler which will listen for input data.
        
def fib_handler(client):
    while True:
        req = client.recv(100)  # waits for data that sent by the client.
        if not req: break
        result = fib(int(req))
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp) # sends data back to the client.
    print("Closed")
    
fib_server(('', 25000))