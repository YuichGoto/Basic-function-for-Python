#! /usr/bin/env python3
#Random Screen for python3 2018.12.10 Y.Goto

from basic import *

#main program

cls()

while 1:
  r=rnd(32*24-1)
  locate(r%32,r//32)
  i=rnd(2)
  if i == 0:
    print('\033[0m ')
  else:
    print('\033[7m ')
  wait(1)
  btn()

'''Orignal BASIC program from IchigoJam Recipe
https://15jamrecipe.jimdo.com/basic/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0/%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E7%94%BB%E9%9D%A2/
Random Screen

' Random Screen | IchigoJam BASIC
' Copyright (c) 2015 Keiichi SHIGA (BALLOON a.k.a. Fu-sen.)
' The MIT License (MIT) - https://gist.github.com/fu-sen/282b65c35d81a7d3b64c

5 'ﾗﾝﾀﾞﾑｶﾞﾒﾝ
10 CLS
20 R=RND(32*24-1)
30 LOCATE R%32,R/32
40 PRINT CHR$(RND(2));
50 GOTO 20
'''
