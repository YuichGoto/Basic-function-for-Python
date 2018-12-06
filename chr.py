#! /usr/bin/python

from basic import *

cls()

for c in range(256):
  locate (c%32 ,c//32,chr(c))

