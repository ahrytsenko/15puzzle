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

    def getPosX(self): return self.pos[0]
    def getPosY(self): return self.pos[1]
    def getSizeX(self): return self.size[0]
    def getSizeY(self): return self.size[1]
    def setPosX(self, x): self.pos[0]=x
    def setPosY(self, y): self.pos[1]=y
    def setSizeX(self, x): self.size[0]=x
    def setSizeY(self, y): self.size[1]=y
    def getPos(self): return list(self.pos)
    def getSize(self): return list(self.size)
    def setPos(self, x, y): 
        self.pos = [x, y]
    def setSize(self, x, y): 
        self.size = [x, y]
    
# Test area
b = Block([10, 10], [30, 30])

print b.size
print b.pos
print b.getPos()
print b.getPosX()
print b.getPosY()
b.setPosX(15)
b.setPosY(25)
print b.getPos()

b.setPos(35, 55)
print b.getPos()
