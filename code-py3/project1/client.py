from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)