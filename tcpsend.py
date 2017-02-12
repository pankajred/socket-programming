#!/usr/bin/env python2

import socket

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#s_ip=raw_input("Enter your server ip :  ")
s1.connect(("192.168.135.134",9999))

while True :
	msg=raw_input("Enter your message :  ")
	s1.send(msg)

s1.close()
