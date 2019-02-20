#!/usr/bin/python          
import sys 
from socket import *  
import json   
import struct
import threading
MCAST_PORT = 5007
MCAST_GRP = '224.1.1.1'
host = 'localhost'  #127.0.0.1
MAX_BUF = 2048   
port = 50000 
addr = (host,port)
s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
topic = dict()
def recvMsg():
  while True:
    recvpack, payload = s.recvfrom(1024)
    t =json.loads(recvpack.decode('utf-8'))
    # print(t)
    for k,v in t.items():
      topic[k] = v
threading.Thread(target = recvMsg, args = ()).start()
while True:
  txtout = sys.stdin.readline().strip()
  command = txtout.split()
  if len(command) > 1 & len(command) <=3 :
    if len(command) == 2:
      if command[0] == 'sub':
        topic[command[1]] = ''
      else:
        print("Invalid command")
    else :
      if command[0] == 'pub':
        topic[command[1]] = command[2]
    data_string = json.dumps(command)
    s.sendto(data_string.encode('utf-8'),addr)  
  if txtout == 'quit':
    break
  if txtout == 'list':
    print(topic)
s.close()   