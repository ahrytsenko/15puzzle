#Description: 15 Puzzle
#Date: 15 FEB 2016
#Author: Andrii Grytsenko
#Programing Language: Python (on-line interpreter www.codeskulptor.org)

import random

class FifteenPuzzleCore:
    def __init__(self, puzzle_size = 4, emptyNumber = 15):
        self.PUZZLE_SIZE = puzzle_size
        self.EMPTY_NUMBER = emptyNumber
        self.lstPlaces = range(self.PUZZLE_SIZE*self.PUZZLE_SIZE)
        self.lstMovablePlaces = []
        self.iFreePlace = 15
        self.iMovements = 0
        self.updateMovablePlaces()
        
    #Private methods
    # getID returns place ID computed by given row and collumn
    def getID(self, aRow, aCol):
        return (aRow*(self.PUZZLE_SIZE) + aCol)

    # getRow returns row where given place 
    def getRow(self, ID):
        return (ID / self.PUZZLE_SIZE)

    def getCol(self, ID):
        return (ID % self.PUZZLE_SIZE)
    
    def updateMovablePlaces(self):
        self.lstMovablePlaces = []
        if self.getRow(self.iFreePlace) > 0:
            self.lstMovablePlaces.append(self.getID(self.getRow(self.iFreePlace)-1, self.getCol(self.iFreePlace)))
        if self.getRow(self.iFreePlace) < self.PUZZLE_SIZE-1:
            self.lstMovablePlaces.append(self.getID(self.getRow(self.iFreePlace)+1, self.getCol(self.iFreePlace)))
        if self.getCol(self.iFreePlace) > 0:
            self.lstMovablePlaces.append(self.getID(self.getRow(self.iFreePlace), self.getCol(self.iFreePlace)-1))
        if self.getCol(self.iFreePlace) < self.PUZZLE_SIZE-1:
            self.lstMovablePlaces.append(self.getID(self.getRow(self.iFreePlace), self.getCol(self.iFreePlace)+1))
    
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
        for placeID in self.lstMovablePlaces:
            if not bPossible:
                bPossible = (placeID == ID)
        return bPossible

    #Description: Exchange IDs of draughts at places "ID of place" and iFreePlace (lstPlaces["ID of place"] <==> lstPlaces[iFreePlace].
    #After that change the ID of free place (iFreePlace = "ID of place") and fresh lstMovableDraughts.
    def moveDraught(self, ID):
        self.lstPlaces[self.iFreePlace] = self.lstPlaces[ID]
        self.lstPlaces[ID] = self.EMPTY_NUMBER
        self.iFreePlace = ID
        self.updateMovablePlaces()
        self.iMovements += 1

    def shuffle(self):
        random.shuffle(self.lstPlaces)
        self.iMovements = 0
        self.iFreePlace = self.lstPlaces.index(self.EMPTY_NUMBER)
        self.updateMovablePlaces()
    
# Test area
fpc = FifteenPuzzleCore(4)
fpc.shuffle()

print fpc.lstPlaces
print fpc.iFreePlace
print fpc.lstMovablePlaces
print fpc.isOrdered()

print "fpc.moveDraught(0)"
if fpc.isMovable(0): 
    fpc.moveDraught(0)
print fpc.lstPlaces
print fpc.iFreePlace
print fpc.lstMovablePlaces
print fpc.isOrdered()

print "fpc.moveDraught(11)"
if fpc.isMovable(11): 
    fpc.moveDraught(11)
print fpc.lstPlaces
print fpc.iFreePlace
print fpc.lstMovablePlaces
print fpc.isOrdered()

print "fpc.moveDraught(6)"
if fpc.isMovable(6): 
    fpc.moveDraught(6)
print fpc.lstPlaces
print fpc.iFreePlace
print fpc.lstMovablePlaces
print fpc.isOrdered()

print "fpc.moveDraught(15)"
if fpc.isMovable(15): 
    fpc.moveDraught(15)
print fpc.lstPlaces
print fpc.iFreePlace
print fpc.lstMovablePlaces
print fpc.isOrdered()

print "fpc.moveDraught(10)"
if fpc.isMovable(10): 
    fpc.moveDraught(10)
print fpc.lstPlaces
print fpc.iFreePlace
print fpc.lstMovablePlaces
print fpc.isOrdered()

print "fpc.moveDraught(0)"
if fpc.isMovable(0): 
    fpc.moveDraught(0)
print fpc.lstPlaces
print fpc.iFreePlace
print fpc.lstMovablePlaces
print fpc.isOrdered()

print "fpc.moveDraught(15)"
if fpc.isMovable(15): 
    fpc.moveDraught(15)
print fpc.lstPlaces
print fpc.lstMovablePlaces
print fpc.isOrdered()
