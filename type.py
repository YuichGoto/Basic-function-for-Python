#! /usr/bin/env python3
#Hispeed typing game for python3 2018.12.04 Y.Goto

from basic import *

#main program

clt()
for n in range(97, 123, 1):
  print (chr(n),end="",flush=True)
  while 1:
    if n == inkey():
      n += 1
      break

print ( '\n',int(tick()/60) )


'''Orignal BASIC program from IchigoJam mini games
https://ichigojam.net/book/IchigoJam-firstgame.pdf
Kousoku typing game

10 N=65:CLT
20 ?CHR$(N);
30 IF INKEY()<>N GOTO 30
40 N=N+1:IF N<>91 GOTO 20
50 ?:?TICK()/60
'''
