#Description: 15 Puzzle
#Date: 24 MAR 2016
#Author: Andrii Grytsenko
#Programing Language: Python (on-line interpreter www.codeskulptor.org)

import simplegui

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
    def setColor(self, color): self.color = list(color)
        
    def append(self, visualBlock):
        self.items.append(visualBlock)
        
    def isSelected(self, pos):
        return (((pos[0] >= self.pos[0]) and (pos[0] < (self.pos[0]+self.size[0]))) and 
                ((pos[1] >= self.pos[1]) and (pos[1] < (self.pos[1]+self.size[1]))))
    
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
        VisualBlock.__init__(self, [size[0], size[1]+size[2]], [0, 0], color, 1)
        self.STR_IN_GAME = "Steps: "
        self.STR_OUT_OF_GAME = "Game over"
        self.frame = frame
        self.EMPTY_NUMBER = empty_number
        self.draughts_mtrx = list(draughts_mtrx)
        self.draught_size = [self.size[0]/self.draughts_mtrx[0], (self.size[1]-size[2])/self.draughts_mtrx[1]]
        self.fpc = FifteenPuzzleCore(draughts_mtrx[0], empty_number)
        self.fpc.shuffle()
        i = 0
        for place in self.fpc.getPlaces():
            self.append(Draught(self.draught_size, self.getDraughtPosByID(i), self.getDraughtColorByNumber(place), 
                                1, self.getDraughtCaptionByNumber(place), i, self.frame))
            i += 1
        self.infoPanel = VisualBlock([size[0], size[2]], [0, size[1]], self.getDraughtColorByNumber(self.EMPTY_NUMBER+1), 1)
        self.infoPanel.append(Draught([size[0], size[2]], [0, size[1]], self.getDraughtColorByNumber(self.EMPTY_NUMBER+1), 1, 
                                      self.STR_IN_GAME+str(self.fpc.iMovements), -1, self.frame))
        
    def getDraughtPosByID(self, ID):
        return [self.pos[0]+(self.draught_size[0]*(ID%self.draughts_mtrx[0])), 
                self.pos[1]+(self.draught_size[1]*(ID/self.draughts_mtrx[0]))]
    
    def getDraughtCaptionByNumber(self, number):
        if (number == self.EMPTY_NUMBER): return ""
        else: return str(number+1)
        
    def getDraughtColorByNumber(self, number):
        if (number == self.EMPTY_NUMBER): return list(self.color)
        else: return [self.color[1], self.color[0]]

    def getDraughtID(self, row, col): return (row*self.draughts_mtrx[0] + col)
    
    def updateDraughts(self):
        for i in range(self.draughts_mtrx[0]*self.draughts_mtrx[1]):
            self.items[i].setCaption(self.getDraughtCaptionByNumber(self.fpc.lstPlaces[i]))
            self.items[i].setColor(self.getDraughtColorByNumber(self.fpc.lstPlaces[i]))
    
    def getSelectedDraughtID(self, pos):
        found = False
        for item in self.items:
            if (not found):
                if item.isSelected(pos):
                    return item.getNumber()
        return -1
    
    def isOrdered(self): return self.fpc.isOrdered()
    
    def isMovable(self, position): return self.fpc.isMovable(self.getSelectedDraughtID(position))
    
    def moveDraught(self, position): self.fpc.moveDraught(self.getSelectedDraughtID(position))
    
    def onDraw(self, canvas):
        VisualBlock.draw(self, canvas)
        self.infoPanel.draw(canvas)
        
    def onMouseClick(self, position):
        if (not self.isOrdered()):
            if (self.isMovable(position)):
                self.moveDraught(position)
                self.updateDraughts()
                if (not self.isOrdered()):
                    self.infoPanel.items[0].setCaption(self.STR_IN_GAME+str(self.fpc.iMovements))
                else:
                    self.infoPanel.items[0].setCaption(self.STR_OUT_OF_GAME)
                
    def onReset(self):
        self.fpc.shuffle()
        self.updateDraughts()
        self.infoPanel.items[0].setCaption(self.STR_IN_GAME+str(self.fpc.iMovements))
        
