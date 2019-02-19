#!/usr/bin/python          
import sys 
from socket import *  
import json   
import struct
MCAST_PORT = 5007
MCAST_GRP = '224.1.1.1'
host = 'localhost'  #127.0.0.1
MAX_BUF = 2048   
port = 50000 
myport = 0
addr = (host,port)
s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
s.settimeout(10)
topic = dict()
while True:
  txtout = sys.stdin.readline().strip()
  command = txtout.split()
  if len(command) > 1 & len(command) <=3 :
    if len(command) == 2:
      if command[0] == 'subscribe':
        topic[command[1]] = ''
      else:
        print("Invalid command")
    else :
      if command[0] == 'publish':
        topic[command[1]] = command[2]
    data_string = json.dumps(command)
    s.sendto(data_string.encode('utf-8'),(host,port))  
  if txtout == 'quit':
    break
  if txtout == 'list':
    print(topic)
  # try:
  #   recvpack, payload = s.recvfrom(1024)
  # except error:
  #   recvpack = None
  # if recvpack is not None:
  #   t =json.loads(recvpack.decode('utf-8'))
  #   for k,v in t.items():
  #     topic[k] = v
s.close()   