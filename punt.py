#! /usr/bin/env python3
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
  scroll(0)
  i=inkeyd()
  if i == LEFT:
    x=x-1
  if i == RIGHT:
    x=x+1
    
  if y < 17:
    y=y+1
  else:
    if rn[0] == x:
      locate(0,23)
      break
    del rn[0]


'''Orignal BASIC program from IchigoJam mini games
https://ichigojam.net/book/IchigoJam-firstgame.pdf
Kawakudari game

10 CLS:X=16
20 LC X,5:?”O”
30 LC RND(32),23:?”*”
35 WAIT 3
36 X=X-BTN(28)+BTN(29)
37 IF SCR(X,5) END
40 GOTO 20
'''