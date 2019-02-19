#!/usr/bin/python          
import sys 
from socket import *  
import json           
host = 'localhost' 
port = 50000                
addr = (host,port)
s = socket(AF_INET, SOCK_DGRAM) 
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
    s.sendto(data_string.encode('utf-8'),addr)
  if txtout == 'quit':
    break
  if txtout == 'list':
    print(topic)
s.close()   