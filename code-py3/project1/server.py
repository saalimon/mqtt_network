#!/usr/bin/python           
from socket import * 
import sys
import json
import threading,os

MCAST_GRP = '224.1.1.1'
host = 'localhost' 
MAX_BUF = 2048     
port = 50000 
MCAST_PORT = 5007
MULTICAST_TTL = 2
addr = (host, port)  
s = socket(AF_INET, SOCK_DGRAM,IPPROTO_UDP) 
s.bind(addr)                
topic = dict()    
list_of_sub = list()
print ('Broker started ...')
def getcmd():
  while True:
    command = sys.stdin.readline().strip()
    if command == 'quit':
      print('Terminate server ...')
      break    
    elif command == 'show':
      data_string = json.dumps("show")
      for i in list_of_sub:
        s.sendto(data_string.encode('utf-8'), i)
    else:
      print("command invalid")
  s.close
  os._exit(1)
threading.Thread(target = getcmd, args = ()).start()
while True:
  txtin,addr = s.recvfrom(MAX_BUF)
  data_loaded = json.loads(txtin.decode('utf-8'))
  print ('Got connection from', addr)
  if txtin == b'quit':          
     print('Terminate server ...')
     break
  if data_loaded[0]=='sub':
    if data_loaded[2] not in topic:
      topic[data_loaded[2]] = ''        #data_loaded[1] is topic_name
      # client_port = json.dumps({'port':addr[1]})
      # s.sendto(client_port.encode('utf-8'),addr)
  elif data_loaded[0]=='pub':
    if data_loaded[2] in topic:
      topic[data_loaded[2]] = data_loaded[3]  #data_loaded[1] is topic_name  
  data_string = json.dumps(topic)
  if addr not in list_of_sub:
    list_of_sub.append(addr)
  for i in list_of_sub:
    s.sendto(data_string.encode('utf-8'), i)
  print(topic)
s.close()      
