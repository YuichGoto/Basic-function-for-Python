#! /usr/bin/env python3
#basic library for python2/3 2018.12.07 Y.Goto

import random
import time
import sys

UP=16
DOWN=14
LEFT=8
RIGHT=12

def rnd(i):
  j=random.randrange(i)
  return (j)

def cls():
  #kb.cls()
  sys.stdout.write ('\033[2J')
  sys.stdout.flush()
  #print ('\033[2J',end="" ,flush=True)
  

def locate(x,y,i=""):
  x = str(x)
  y = str(y)
  sys.stdout.write ('\033['+y+';'+x+'H'+i)
  sys.stdout.flush()
  #print ('\033['+y+';'+x+'H'+i,end="" ,flush=True) 
  
def scroll(ud=0):
  ud = str(ud)
  if ud == '0':
    sys.stdout.write ('\033[s\033[0;0H\033[M\033[u\033[A')
    #sys.stdout.write ('\033[S')
  if ud == '2':
    sys.stdout.write ('\033[s\033[0;0H\033[L\033[u')
    #sys.stdout.write ('\033[T')
  sys.stdout.flush()

def btn(a=0):
  i=kb.kbhit()
  if (i):
    j = ord (kb.getch())
    if ( j == 27 ):
      sys.stdout.write ('\033[0m   ESC break\n')
      #print('\033[0m   ESC break')
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
    sys.stdout.write ('\033[0m   ESC break\n')
    #print('\033[0m   ESC break')
    exit(0)
  return i

def inkey():
  i = ord( kb.getch() )
  if ( i == 27 ):
    sys.stdout.write ('\033[0m   ESC break\n')
    #print('\033[0m   ESC break')
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



#Class KBHit 
#Down load from http://home.wlu.edu/~levys/software/kbhit.py 2018.12.02 Y.Goto
'''
A Python class implementing KBHIT, the standard keyboard-interrupt poller.
Works transparently on Windows and Posix (Linux, Mac OS X).  Doesn't work
with IDLE.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
'''

import os
# Windows
if os.name == 'nt':
    import msvcrt
# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select

class KBHit:
    
    def __init__(self):
        '''Creates a KBHit object that you can call to do various keyboard things.
        '''

        if os.name == 'nt':
            pass
        
        else:
    
            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)
    
            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
    
            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)
    
    
    def set_normal_term(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''
        
        if os.name == 'nt':
            pass
        
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)


    def getch(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''
        
        s = ''
        
        if os.name == 'nt': #add arrow up:^p down:^n right:^l left:^h Y.Goto 2018.12.04
            #return msvcrt.getch().decode('utf-8')
            
            i = msvcrt.getch()
            if i == b'\xe0':
                i = msvcrt.getch()
                if i == b'H': #up    ctrl-p
                  i = chr(0x10)
                if i == b'P': #down  ctrl-n
                  i = chr(0x0e)
                if i == b'K': #left  ctrl-h
                  i = chr(0x08)
                if i == b'M': #right ctrl-l
                  i = chr(0x0c)
            else:
              i=i.decode('utf-8')
            return i
        else:
            #return sys.stdin.read(1)
           i = sys.stdin.read(1)
           #if i == b'\x1b':
           if i == chr(27):
             i = sys.stdin.read(1)
             #if i == b'\x1b': #ESC
             if i == chr(27):
               i = b'\x1b'
               return i
             i = sys.stdin.read(1)
             #if i == b'A': #up    ctrl-p
             if i == (chr(65)):
               i = chr(0x10)
             #if i == b'B': #down  ctrl-n
             if i == (chr(66)):
               i = chr(0x0e)
             #if i == b'D': #left  ctrl-h
             if i == (chr(68)):
               i = chr(0x08)
             #if i == b'C': #right ctrl-l
             if i == (chr(67)):
               i = chr(0x0c)
           return i


    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()
        
        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []

#add clear screen Y.Goto 2018.12.02

    def cls(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            os.system('CLS')
            return (0)
        
        else:
            os.system('clear') 
            return dr != []

kb = KBHit()
