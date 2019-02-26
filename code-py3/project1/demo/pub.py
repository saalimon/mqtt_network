#!/usr/bin/python          
import sys 
from socket import *  
import json   
import struct
import threading,os
MCAST_PORT = 5007
MCAST_GRP = '224.1.1.1'
host = 'localhost'  #127.0.0.1
MAX_BUF = 2048   
port = 50000 
addr = (host,port)
s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
s.bind(('',0))
topic = dict()
while True:
  txtout = sys.stdin.readline().strip()
  command = txtout.split()
  if len(command) ==4 :
    if command[0] == 'pub':
        address = command[1]
        topic[command[2]] = command[3]
    else:
        print("Invalid command")
    addr = (address,port)
    data_string = json.dumps(command)
    s.sendto(data_string.encode('utf-8'),addr)  
  elif txtout == 'quit':
    print("Client close ....")
    break
  elif txtout == 'list':
    print(topic)
  else:
    print("Invalid command")
s.close() 