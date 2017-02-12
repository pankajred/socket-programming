#!/usr/bin/env python2

import socket 

s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s1.bind(("",9999))
s1.listen(6)

c_socket,c_adder=s1.accept()

while True :
	print c_socket.recv(100)



s1.close
