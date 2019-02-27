#!/usr/bin/python          
import sys 
from socket import *  
import json   
import struct
import threading,os
host = 'localhost'  #127.0.0.1
MAX_BUF = 2048   
port = 50000 
s = socket(AF_INET, SOCK_STREAM)
topic = dict()
list_of_sub = list()
def subMsg():
  while True:
    recvpack,addr = s.recvfrom(1024)
    # if(t == 'hello')
    t =json.loads(recvpack.decode('utf-8'))
    if(t == 'show'):
        print(topic)
    else:
        for k,v in t.items():
            if k in topic:
                topic[k] = v
        # print(topic)
    print(addr)
while True:
    while True:
        txtout = input('subscriber : ')
        txtout = txtout.strip()
        command = txtout.split()
        if len(command) == 3 :
            if command[0] == 'sub':
                address = command[1]
                topic[command[2]] = ''
                addr = (address,port)
                print(addr)
                s.connect(addr)
                # threading.Thread(target = subMsg, args = ()).start()
                break
            else:
                print("Invalid command : use subscribe broaker_ip topic_name")
        elif txtout == 'quit':
            print("Client close ....")
            s.close() 
            os._exit(1) 
            break
        elif txtout == 'list':
            print(topic)
        else:
            print("Invalid command")
    addr = (address,port)
    data_string = json.dumps(command)
    s.sendto(data_string.encode('utf-8'),addr)  
    while True:
        recvpack = s.recv(1024)
        t =json.loads(recvpack.decode('utf-8'))
        if t == 'show':
            print(topic)
        else:
            for k,v in t.items():
                if k in topic:
                    topic[k] = v
s.close() 
os._exit(1) #must have s.close() before 