#! /usr/bin/env python3
#screen jack for python3 2018.12.04 Y.Goto

from basic import *

#main program

cls()
c=32

while 1:
  k=inkeyd()
  if k != 0:
    c=k
  if c == 32:
    print('\033[7m')
  locate(rnd(32),rnd(22))
  print(chr(c)+'\033[0m')
  wait(10)


'''Orignal BASIC program from IchigoJam mini games
https://ichigojam.net/book/IchigoJam-firstgame.pdf

10 CLS:C=1
20 LC RND(32),RND(22)
30 ?CHR$(C)
40 K=INKEY():IF K C=K
50 GOTO 20
'''
