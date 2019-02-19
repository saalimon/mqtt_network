#!/usr/bin/python           
from socket import * 
import sys
import json

host = 'localhost' 
MAX_BUF = 2048     
port = 50000 
addr = (host, port)  
s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP) 
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) 
s.bind(addr)                
topic = dict()    
print ('Broker started ...')
while True:
  txtin,addr = s.recvfrom(MAX_BUF)
  data_loaded = json.loads(txtin.decode('utf-8'))
  print ('Got connection from', addr)
  if txtin == b'quit':          
     print('Terminate server ...')
     break
  if data_loaded[0]=='subscribe':
    if data_loaded[1] not in topic:
      topic[data_loaded[1]] = ''        #data_loaded[1] is topic_name
  elif data_loaded[0]=='publish':
    if data_loaded[1] in topic:
      topic[data_loaded[1]] = data_loaded[2]  #data_loaded[1] is topic_name
  print(topic)
  # data_string = json.dumps(topic)
  # s.sendto(data_string.encode('utf-8'), addr)

s.close()      
