#! /usr/bin/env python3
#addition game for python3 2018.12.04 Y.Goto

from basic import *

#main program

clt()
for i in range(10):
  a=rnd(10)
  b=rnd(10)
  print(a,'+',b,'= ',end="")
  c=int(input())
  if c != a+b:
    print('NG!')
    break

print ( int(tick()/60) )

'''Orignal BASIC program from IchigoJam mini games
https://ichigojam.net/book/IchigoJam-firstgame.pdf
Tasizan meijin game

10 N=0:CLT
20 A=RND(10)
30 B=RND(10)
40 ?A;”+”;B;”=“;:INPUT C
50 IF C!=A+B ?”NG!”:END
60 N=N+1:IF N<10 GOTO 20
70 ?TICK()/60
'''