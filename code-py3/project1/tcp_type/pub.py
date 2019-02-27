#!/usr/bin/python          
import sys 
from socket import *  
import json   
import struct
import threading,os
host = 'localhost'  #127.0.0.1
MAX_BUF = 2048   
port = 50000 
# s = socket(AF_INET, SOCK_STREAM)
topic = dict()
while True:
    while True:
        txtout = input('publisher : ')
        txtout = txtout.strip()
        command = txtout.split()
        if len(command) == 4 :
            if command[0] == 'pub':
                address = command[1]
                topic[command[2]] = command[3]   
                addr = (address,port)
                s = socket(AF_INET, SOCK_STREAM)
                s.connect(addr)             
                break
            else:
                print("Invalid command : use publish broaker_ip topic_name value")
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
    data_string = json.dumps(command).encode('utf-8')
    s.sendall(data_string)
    s.close()
s.close() 
os._exit(1) #must have s.close() before 