#! /usr/bin/python

from basic import *
import time

#main program

clt()
for n in range(97, 123, 1):
  print (chr(n),end="",flush=True)
  while 1:
    if n == inkey():
      n += 1
      break

print ( '\n',int(tick()/60) )

