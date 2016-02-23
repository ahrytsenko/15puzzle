#Description: 15 Puzzle
#Date: 15 FEB 2016
#Author: Andrii Grytsenko
#rograming Language: Python (on-line interpreter www.codeskulptor.org)


import simplegui
import random

WIDTH = 320
HEIGHT = 320
EMPTY_NUMBER = 15

vb = None
draughts = None

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
    def __init__(self, size, color, frame, empty_number, draughts_mtrx):
        VisualBlock.__init__(self, size, [0, 0], color, 1)
        self.frame = frame
        self.EMPTY_NUMBER = empty_number
        self.draughts_mtrx = list(draughts_mtrx)
        self.draught_size = [self.size[0]/4, self.size[1]/4]
        for col in range(self.draughts_mtrx[0]):
            for row in range(self.draughts_mtrx[1]):
                if (self.getDraughtID(row, col) == self.EMPTY_NUMBER):
                    tmp_color = list(self.color)
                    tmp_caption = ""
                else:
                    tmp_color = [self.color[1], self.color[0]]
                    tmp_caption = str(self.getDraughtID(row, col)+1)
                self.append(Draught(self.draught_size, self.getDraughtPosByID(self.getDraughtID(row, col)), tmp_color, 1, tmp_caption, self.getDraughtID(row, col), self.frame))
        
    def getDraughtPosByID(self, ID):
        return [self.pos[0]+(self.draught_size[0]*(ID%self.draughts_mtrx[0])), 
                self.pos[1]+(self.draught_size[1]*(ID/self.draughts_mtrx[1]))]

    def getDraughtID(self, row, col): return (row*self.draughts_mtrx[1] + col)


# Handler to draw on canvas
def draw(canvas):
    global draughts
    draughts.draw(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# Test area
draughts = Draughts([WIDTH, HEIGHT], ["White", "Green"], frame, EMPTY_NUMBER, [4, 4])
