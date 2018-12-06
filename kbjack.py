#! /usr/bin/python
#keyboad jack for python3 2018.12.04 Y.Goto

from basic import *

#main program
c=32
cls()

while 1:
  k=inkeyd()
  if k != 0:
    c=k
  if c == 32:
    print('\033[7m')

  locate(rnd(32),rnd(22))
  print(chr(c)+'\033[0m')
  wait(10)
