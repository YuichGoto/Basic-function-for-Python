#! /usr/bin/env python3
#space ship tour game for python3 2018.12.09 Y.Goto

from basic import *

#main program

cls()

x,y,y1=15,18,1
rn=[]

while 1:
  locate(x,y,'A')
  wait(10)
  locate(x,y,' ')
  rn=rn+([rnd(32)])
  scroll(2)
  locate(rn[-1],0,'o')
  i=inkeyd()
  if i == LEFT:
    x=x-1
  if i == RIGHT:
    x=x+1
  if i == UP:
    y=y-1
  if i == DOWN:
    y=y+1

  if y1 >= y:
    if rn[y1-y] == x:
      locate(x,y,'*')
      locate(15,12,'CRASH!')
      locate(0,23)
      break

  if y1 < y+1:
    y1=y1+1
  else:
    del rn[0]


'''Orignal BASIC program from IchigoJam mini games
http://kidspod.club/program/default.html?id=701
SPACE SHIP game

10 'SPACE SHIP
20 CLS
30 X=15:Y=18
40 @LP
50 LCX,Y:?CHR$(0);
60 X=X-BTN(LEFT)+BTN(RIGHT)
70 Y=Y-BTN(UP)+BTN(DOWN)*2
80 SCROLL 2
90 IFSCR(X,Y)<>0GOTO@ED
100 LCX,Y:?"A";
110 LCRND(32),0:?"O";
120 WAIT5
130 GOTO@LP
140 @ED:LCX,Y:?"*";
150 LC10,10:?"CRASH!";
160 @W:K=INKEY():IFK=0GOTO@W
170 IFK=10RUN
180 IFK=32CLS:END
190 GOTO@W
'''
