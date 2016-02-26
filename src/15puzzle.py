#Description: 15 Puzzle
#Date: 25 FEB 2016
#Author: Andrii Grytsenko
#rograming Language: Python (on-line interpreter www.codeskulptor.org)

import simplegui
import random

WIDTH = 320
HEIGHT = 320
EMPTY_NUMBER = 15
PUZZLE_DIMENSION = 4
PUZZLE_COLORS = ["White", "Green"]

draughts = None

class FifteenPuzzleCore:
    def __init__(self, puzzle_size = 4, free_place = 15):
        self.PUZZLE_SIZE = puzzle_size
        self.FREE_PLACE = free_place
        self.lstPlaces = []
        self.lstPlaces = range(self.PUZZLE_SIZE*self.PUZZLE_SIZE)
        self.lstMovableDraughts = []
        self.iFreePlace = 15
        self.iMovements = 0
        self.updateMovableDraughts()
        
    #Private methods
    def __str__(self):
        pass
        #return "Draughts: " + self.lstPlaces + 

    def getID(self, aRow, aCol):
        return (aRow*(self.PUZZLE_SIZE) + aCol)

    def getRow(self, ID):
        return (ID / self.PUZZLE_SIZE)

    def getCol(self, ID):
        return (ID % self.PUZZLE_SIZE)
    
    def updateMovableDraughts(self):
        self.lstMovableDraughts = []
        if self.getRow(self.iFreePlace) > 0:
            self.lstMovableDraughts.append(self.getID(self.getRow(self.iFreePlace)-1, self.getCol(self.iFreePlace)))
        if self.getRow(self.iFreePlace) < self.PUZZLE_SIZE-1:
            self.lstMovableDraughts.append(self.getID(self.getRow(self.iFreePlace)+1, self.getCol(self.iFreePlace)))
        if self.getCol(self.iFreePlace) > 0:
            self.lstMovableDraughts.append(self.getID(self.getRow(self.iFreePlace), self.getCol(self.iFreePlace)-1))
        if self.getCol(self.iFreePlace) < self.PUZZLE_SIZE-1:
            self.lstMovableDraughts.append(self.getID(self.getRow(self.iFreePlace), self.getCol(self.iFreePlace)+1))
    
    #Public methods
    
    def getMovements(self): return self.iMovements
    def getPlaces(self): return list(self.lstPlaces)
    
    #Description: Check if all graughts are at the right places. 
    #Simply to check if ID of place is equal to ID of draught at that place (lstPlaces[i] == i)
    def isOrdered(self):
        bOrdered = True
        for i in range(len(self.lstPlaces)):
            if bOrdered:
                bOrdered = (self.lstPlaces[i] == i)
        return bOrdered

    #Description: Check if is it possible to move a draught from selected place to a free place. 
    #As we have a list of such places (lstMovableDraughts) the task is to check if selected ID is in the list.
    def isMovable(self, ID):
        bPossible = False
        for placeID in self.lstMovableDraughts:
            if not bPossible:
                bPossible = (placeID == ID)
        return bPossible

    #Description: Exchange IDs of draughts at places "ID of place" and iFreePlace (lstPlaces["ID of place"] <==> lstPlaces[iFreePlace].
    #After that change the ID of free place (iFreePlace = "ID of place") and fresh lstMovableDraughts.
    def moveDraught(self, ID):
        self.lstPlaces[self.iFreePlace] = self.lstPlaces[ID]
        self.lstPlaces[ID] = self.FREE_PLACE
        self.iFreePlace = ID
        self.updateMovableDraughts()
        self.iMovements += 1

    def shuffle(self):
        random.shuffle(self.lstPlaces)
        self.iMovements = 0
        self.iFreePlace = self.lstPlaces.index(self.FREE_PLACE)
    
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
        VisualBlock.__init__(self, size, [0, 0], color, 1)
        self.frame = frame
        self.EMPTY_NUMBER = empty_number
        self.draughts_mtrx = list(draughts_mtrx)
        self.draught_size = [self.size[0]/self.draughts_mtrx[0], self.size[1]/self.draughts_mtrx[1]]
        self.fpc = FifteenPuzzleCore(draughts_mtrx[0], empty_number)
        self.fpc.shuffle()
        i = 0
        for place in self.fpc.getPlaces():
            self.append(Draught(self.draught_size, self.getDraughtPosByID(i), self.getDraughtColorByNumber(place), 
                                1, self.getDraughtCaptionByNumber(place), i, self.frame))
            i += 1
        
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
            #self.items[i].setNumber(self.fpc.lstPlaces[i])
    
    def getSelectedDraughtID(self, pos):
        found = False
        for item in self.items:
            if (not found):
                if item.isSelected(pos):
                    return item.getNumber()
        return -1

# Handler for mouse
def mouse_handler(position):
    global draughts
    print draughts.getSelectedDraughtID(position)
    print draughts.fpc.iFreePlace
    print draughts.fpc.lstMovableDraughts
    if (draughts.fpc.isMovable(draughts.getSelectedDraughtID(position))):
        draughts.fpc.moveDraught(draughts.getSelectedDraughtID(position))
        draughts.updateDraughts()
    
# Handler to draw on canvas
def draw(canvas):
    global draughts
    draughts.draw(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

# Test area
draughts = Draughts([WIDTH, HEIGHT], PUZZLE_COLORS, frame, EMPTY_NUMBER, [PUZZLE_DIMENSION, PUZZLE_DIMENSION])
