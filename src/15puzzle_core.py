#Description: 15 Puzzle
#Date: 15 FEB 2016
#Author: Andrii Grytsenko
#rograming Language: Python (on-line interpreter www.codeskulptor.org)

import simplegui

PUZZLE_SIZE = 4
IDX_MIN = 0
IDX_MAX = PUZZLE_SIZE-1

class FPuzzle:
    def __init__(self, puzzle_size = 4):
        self.PUZZLE_SIZE = puzzle_size
        self.lstPlaces = []
        for i in range(self.PUZZLE_SIZE*self.PUZZLE_SIZE):
            self.lstPlaces.append(i)
        self.lstMovableDraughts = []
        self.iFreePlace = 0
        self.iMovements = 0

#Name: isOrdered
#In: lst
#Out: boolean
#Description: Check if all graughts are at the right places. 
#Simply to check if ID of place is equal to ID of draught at that place (lstPlaces[i] == i)
    def isOrdered(self):
        bOrdered = True
        for i in range(len(self.lstPlaces)):
            if bOrdered:
                bOrdered = (self.lstPlaces[i] == i)
        return bOrdered

#Name: isMovable
#In: ID
#Out: boolean
#Description: Check if is it possible to move a draught from selected place to a free place. 
#As we have a list of such places (lstMovableDraughts) the task is to check if selected ID is in the list.
    def isMovable(self, ID):
        bPossible = False
        for placeID in self.lstMovableDraughts:
            if not bPossible:
                bPossible = (placeID == ID)
        return bPossible

#Name: moveDraught
#In: lstPlaces, "ID of place"
#Out: none
#Description: Exchange IDs of draughts at places "ID of place" and iFreePlace (lstPlaces["ID of place"] <==> lstPlaces[iFreePlace].
#After that change the ID of free place (iFreePlace = "ID of place") and fresh lstMovableDraughts.
    def moveDraught(self, ID):
        pass

    def getID(self, aRow, aCol):
        return (aRow*(self.PUZZLE_SIZE) + aCol)

    def getRow(self, ID):
        return (ID / self.PUZZLE_SIZE)

    def getCol(self, ID):
        return (ID % self.PUZZLE_SIZE)
    


# Test area
PUZZLE_SIZE = 4
IDX_MIN = 0
IDX_MAX = PUZZLE_SIZE-1

fp = FPuzzle(4)

print fp.lstPlaces
print fp.isOrdered()

#lstMovableDraughts = []
iFreePlace = 15
#iMovements = 0

print fp.getID(0, 0)
print fp.getID(2, 2)
print fp.getID(3, 0)
print ""
print fp.getRow(5)
print fp.getRow(1)
print fp.getRow(15)
print ""
print fp.getCol(5)
print fp.getCol(1)
print fp.getCol(15)



