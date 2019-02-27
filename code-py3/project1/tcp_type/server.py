
from socket import * 
import threading
import os,sys
import json

SERV_PORT = 50000
MAX_BUF = 2048
topic = dict()
list_sub = {}

def main():
  addr = ('127.0.0.1', SERV_PORT)
  s = socket(AF_INET, SOCK_STREAM)
  s.bind(addr)
  s.listen(5)
  print ('Broker started ...')
  while True:
    subs, addr = s.accept()
    ip, port = str(addr[0]), str(addr[1]) 
    print ('New cliebt connected from ..' + ip + ':' + port)
    txtin = subs.recv(MAX_BUF)
    data_loaded = json.loads(txtin)
    if data_loaded[0] == 'sub':
      if subs not in list_sub:
        list_sub[data_loaded[2],port] = subs #data_loaded[2] is topic
        if data_loaded[2] not in topic:
          topic[data_loaded[2]] = ''
    elif data_loaded[0] == 'pub':
      if data_loaded[2] in topic:
        topic[data_loaded[2]] = data_loaded[3] 
        data_string = json.dumps(topic)
        for k,v in list_sub.items():
          v.send(data_string.encode('utf-8'))
        print(topic)
  s.close()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print ('Interrupted ..')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
  s.close()
  
