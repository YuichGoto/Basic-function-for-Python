#! /usr/bin/python
#basic library for python3 2018.12.04 Y.Goto

from kb import kb
import random
import time

def rnd(i):
  j=random.randrange(i)
  return (j)

def cls():
  #kb.cls()
  print ('\033[2J',end="" ,flush=True)

def locate(x,y,i=""):
  x = str(x)
  y = str(y)
  print ('\033['+y+';'+x+'H'+i,end="" ,flush=True) 

def btn(a=0):
  i=kb.kbhit()
  if (i):
    j = ord (kb.getch())
    if ( j == 27 ):
      print('\033[0m   ESC break')
      exit(0)
    if ( a == 0 ):
      i=1
    elif ( j == a ):
      i=1
    else:
      i=0
  return i

def inkeyd():
  i=kb.kbhit()
  if (i):
    i = ord( kb.getch())
  if ( i == 27 ):
    print('\033[0m   ESC break')
    exit(0)
  return i

def inkey():
  i = ord( kb.getch() )
  if ( i == 27 ):
    print('\033[0m   ESC break')
    exit(0)
  return (i)

def wait(i):
  time.sleep(float(i)/60)

def clt():
  global tick_val
  tick_val=time.time()

def tick():
  global tick_val
  return(int((time.time()-tick_val)*60))

