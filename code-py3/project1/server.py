from socket import * 
import sys

SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(1)
print ('TCP server started ...')
