#! /usr/bin/python
#punting tour game for python3 2018.12.04 Y.Goto

from basic import *

#main program

cls()

x,y=16,0
rn=[]

while 1:
  locate(x,5,'0')
  rn=rn+([rnd(32)])
  locate(rn[-1],23,'*')
  wait(10)
  locate(0,0,'\033[1M')

  i=inkeyd()
  if i == 8:
    x=x-1
  if i == 12:
    x=x+1
    
  if y < 17:
    y=y+1
  else:
    if rn[0] == x:
      locate(0,23)
      break
    del rn[0]
