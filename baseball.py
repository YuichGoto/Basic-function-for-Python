#baseball game for python3 2018.12.04 Y.Goto

from basic import *

#main program

for Y in range(23):
  cls()
  locate(4,15,'%')
  locate(5,Y,'0')
  wait(10)

  if btn():
    if Y == 15:
      locate(4,17,'HIT!')
    break
