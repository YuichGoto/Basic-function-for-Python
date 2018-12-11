#! /usr/bin/env python3
#running game for python3 2018.12.10 Y.Goto

from basic import *

#main program

clt()
x=0

cls()

while 1:
  locate(x,15,'o')
  i=inkeyd()

  while i != LEFT:
    i=inkeyd()
  locate(x,15,'0')
  
  while i != RIGHT:
    i=inkeyd()

  if x > 30:
    break
  x=x+1

t=int(tick()*10/6)
print ( '\n',t/100,'sec')
print( int(10800/t),'km/h' )


'''Orignal BASIC program from 福野泰介の一日一創 - create every day
http://fukuno.jig.jp/2325?fbclid=IwAR1VIHM-iBBdYgTZzN2WpzHiZDjJa20IwZmhvEiLzrCQRVJ_awABVjFS8q8
30mSoo game

10 CLT:X=0
20 CLS:LC X,15:?CHR$(252)
30 IF INKEY()!=28 CONT
35 LC X,15:?CHR$(251)
40 IF INKEY()!=29 CONT
50 X=X+1
60 IF X<30 GOTO 20
70 T=TICK()*10/6
80 ?T/100;".";T/10%10;T%10;"sec"
90 V=10800/T:?V;"km/h"
'''