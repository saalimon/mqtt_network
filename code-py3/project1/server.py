#!/usr/bin/python           
from socket import * 
import sys
import json

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number
addr = ('localhost', SERV_PORT)  # Socket address
s = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
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
    topic[data_loaded[1]] = data_loaded[2]  #data_loaded[1] is topic_name
  print(topic)

s.close()      
