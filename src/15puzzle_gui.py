#Description: 15 Puzzle
#Date: 15 FEB 2016
#Author: Andrii Grytsenko
#rograming Language: Python (on-line interpreter www.codeskulptor.org)


import simplegui
import random

WIDTH = 80
HEIGHT = 80
EMPTY_NUMBER = 15

vb = None

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
    def setPos(self, x, y): self.pos = [x, y]
    def setSize(self, x, y): self.size = [x, y]
    def getTopLeft(self): return self.getPos()
    def getTopRight(self) : return [self.getPosX()+self.getSizeX(), self.getPosY()]
    def getBottomRight(self): return [self.getPosX()+self.getSizeX(), self.getPosY()+self.getSizeY()]
    def getBottomLeft(self): return [self.getPosX(), self.getPosY()+self.getSizeY()]
    def getPolygon(self): return [self.getTopLeft(), self.getTopRight(), self.getBottomRight(), self.getBottomLeft()]
    
class VisualBlock(Block):
    def __init__(self, size, pos, color, borderWidth):
        Block.__init__(self, size, pos)
        self.color = list(color)
        self.borderWidth = borderWidth
        self.items = []
        
    def getBlockColor(self): return self.color[0]
    def getBorderColor(self): return self.color[1]
    def getColor(self): return list(self.color)
    def getBorderWidth(self): return self.borderWidth
    def setBlockColor(self, blockColor): self.color[0] = blockColor
    def setBorderColor(self, borderColor): self.color[0] = borderColor
    def setColor(self, blockColor, borderColor): self.color = [blockColor, borderColor]
        
    def append(self, visualBlock):
        self.items.append(visualBlock)
    
    def draw(self, canvas):
        canvas.draw_polygon(self.getPolygon(), self.getBorderWidth(), self.getBorderColor(), self.getBlockColor())
        for item in self.items: item.draw(canvas)
            
class Draught(VisualBlock):
    def __init__(self, size, pos, color, borderWidth, caption, number, frame):
        VisualBlock.__init__(self, size, pos, color, borderWidth)
        self.caption = caption
        self.number = number
        self.frame = frame
        
    def getCaption(self): return self.caption
    def getNumber(self): return self.number
    def setCaption(self, caption): self.caption = caption
    def setNumber(self, number): self.number = number
    def getCaptionPosition(self):
        cp = self.getBottomLeft()
        cp[0] += (self.getSizeX()-self.frame.get_canvas_textwidth(self.caption, self.getSizeY()))/2
        cp[1] -= self.getSizeY()/8
        return list(cp)
        
    def draw(self, canvas):
        VisualBlock.draw(self, canvas)
        canvas.draw_text(self.caption, self.getCaptionPosition(), self.getSizeY(), self.getBorderColor())
    
class Draughts(VisualBlock):
    def __init__(self, size, color, frame):
        VisualBlock.__init__(self, size, [0, 0], color, 1)
        self.frame = frame
    
    
# Handler to draw on canvas
def draw(canvas):
    global vb
    vb.draw(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# Test area
vb = VisualBlock([WIDTH, HEIGHT], [0, 0], ["White", "Green"], 1)
vb2 = Draught([WIDTH/2, HEIGHT/2], [WIDTH/2, HEIGHT/2], ["Green", "Yellow"], 1, "12", 12, frame)
vb.append(vb2)
