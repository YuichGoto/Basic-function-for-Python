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
    exit()

print ( int(tick()/60) )
