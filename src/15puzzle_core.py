#Description: 15 Puzzle
#Date: 15 FEB 2016
#Author: Andrii Grytsenko
#rograming Language: Python (on-line interpreter www.codeskulptor.org)

import simplegui

lstPlaces = []
lstMovableDraughts = []
iFreePlace = 0
iMovements = 0
PUZZLE_SIZE = 4
IDX_MIN = 0
IDX_MAX = PUZZLE_SIZE-1

#Name: isOrdered
#In: lst
#Out: boolean
#Description: Check if all graughts are at the right places. 
#Simply to check if ID of place is equal to ID of draught at that place (lstPlaces[i] == i)
def isOrdered(aList):
    bOrdered = True
    for i in range(len(aList)):
        if bOrdered:
            bOrdered = (aList[i] == i)
    return bOrdered

#Name: isMovable
#In: ID
#Out: boolean
#Description: Check if is it possible to move a draught from selected place to a free place. 
#As we have a list of such places (lstMovableDraughts) the task is to check if selected ID is in the list.
def isMovable(aList, ID):
    bPossible = False
    for placeID in aList:
        if not bPossible:
            bPossible = (placeID == ID)
    return bPossible

#Name: moveDraught
#In: lstPlaces, "ID of place"
#Out: none
#Description: Exchange IDs of draughts at places "ID of place" and iFreePlace (lstPlaces["ID of place"] <==> lstPlaces[iFreePlace].
#After that change the ID of free place (iFreePlace = "ID of place") and fresh lstMovableDraughts.
def moveDraught(aList, ID):
    pass

def getID(aRow, aCol, aSize):
    return (aRow*(aSize) + aCol)
    
def getRow(ID, aSize):
    return (ID / aSize)
    
def getCol(ID, aSize):
    return (ID % aSize)
    


# Test area
PUZZLE_SIZE = 4
IDX_MIN = 0
IDX_MAX = PUZZLE_SIZE-1

for i in range(PUZZLE_SIZE*PUZZLE_SIZE):
    lstPlaces.append(i)

print lstPlaces
print isOrdered(lstPlaces)

#lstMovableDraughts = []
#iFreePlace = 0
#iMovements = 0

print getID(0, 0, PUZZLE_SIZE)
print getID(2, 2, PUZZLE_SIZE)
print getID(3, 0, PUZZLE_SIZE)
print ""
print getRow(5, PUZZLE_SIZE)
print getRow(1, PUZZLE_SIZE)
print getRow(15, PUZZLE_SIZE)
print ""
print getCol(5, PUZZLE_SIZE)
print getCol(1, PUZZLE_SIZE)
print getCol(15, PUZZLE_SIZE)



