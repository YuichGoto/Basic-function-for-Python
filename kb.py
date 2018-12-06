#!/usr/bin/env python
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


Down load from http://home.wlu.edu/~levys/software/kbhit.py 2018.12.02 Y.Goto
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
        
        if os.name == 'nt':
        #-----
        #add arrow up:^p down:^n right:^l left:^h Y.Goto 2018.12.04
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
        #------
        else:
            #return sys.stdin.read(1)
        #------
           i = sys.stdin.read(1)
           if i == b'\x1b':
             i = sys.stdin.read(1)
             if i == b'\x1b': #ESC
               i = b'\x1b'
               return i
             i = sys.stdin.read(1)
             if i == b'A': #up    ctrl-p
               i = chr(0x10)
             if i == b'B': #down  ctrl-n
               i = chr(0x0e)
             if i == b'D': #left  ctrl-h
               i = chr(0x08)
             if i == b'C': #right ctrl-l
               i = chr(0x0c)
           return i
        #------


    def getarrow(self):
        ''' Returns an arrow-key code after kbhit() has been called. Codes are
        0 : up
        1 : right
        2 : down
        3 : left
        Should not be called in the same program as getch().
        '''
        
        if os.name == 'nt':
            msvcrt.getch() # skip 0xE0
            c = msvcrt.getch()
            vals = [72, 77, 80, 75]
            
        else:
            c = sys.stdin.read(3)[2]
            vals = [65, 67, 66, 68]
        
        return vals.index(ord(c.decode('utf-8')))
        

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



kb = KBHit()  #add by Y.Goto 2018.12.02

'''    Comment out by Y.Goto 2018.12.02
# Test    
if __name__ == "__main__":
    
    kb = KBHit()

    print('Hit any key, or ESC to exit')

    while True:

        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 27: # ESC
                break
            print(c)
             
    kb.set_normal_term()
'''
