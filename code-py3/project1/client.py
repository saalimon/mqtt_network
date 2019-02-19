#!/usr/bin/python          
import sys 
from socket import *  
import json   
import struct

host = 'localhost' 
MAX_BUF = 2048    
port = 50000       
addr = (host,port)
s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) 

topic = dict()
while True:
  # print(s.recv(10240))
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
    s.sendto(data_string.encode('utf-8'),addr)
    # print(s.recv(MAX_BUF))
  if txtout == 'quit':
    break
  if txtout == 'list':
    print(topic)
s.close()   