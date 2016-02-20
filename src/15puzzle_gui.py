#Description: 15 Puzzle
#Date: 15 FEB 2016
#Author: Andrii Grytsenko
#rograming Language: Python (on-line interpreter www.codeskulptor.org)

import simplegui
import random

class Block:
    def __init__(self, size, pos):
        self.size = list(size)
        self.pos = list(pos)

    
# Test area
b = Block([10, 10], [30, 30])

print b
print b.size
print b.pos
