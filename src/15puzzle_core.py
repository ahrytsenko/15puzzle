#Description: 15 Puzzle
#Date: 15 FEB 2016
#Author: Andrii Grytsenko
#rograming Language: Python (on-line interpreter www.codeskulptor.org)

import simplegui

lstPlaces = []
lstMovableDraughts = []
Name: iFreePlace = 0
Type: integer
Description: ID of a free place

Name: iMovements
Type: integer
Description: Movements were made since the start solving the current puzzle 

Name: PUZZLE_SIZE
Type: constant (integer)
Description: Amount of rows (and colls cause its are equal). In classical game it is equal to 4

Name: IDX_MIN
Type: constant (integer, usually equals to 0)
Description: Minimal index of array

Name: IDX_MAX
Type: constant (integer, compute from PUZZLE_SIZE, usually equals to PUZZLE_SIZE-1)
Description: Maximal index of array
/////////////////////////////

Section 2. Core functions
Name: isOrdered
In: lst
Out: boolean
Description: Check if all graughts are at the right places. 
Simply to check if ID of place is equal to ID of draught at that place (lstPlaces[i] == i)

Name: isMovable
In: ID
Out: boolean
Description: Check if is it possible to move a draught from selected place to a free place. 
As we have a list of such places (lstMovableDraughts) the task is to check if selected ID is in the list.

Name: moveDraught
In: lstPlaces, "ID of place"
Out: none
Description: Exchange IDs of draughts at places "ID of place" and iFreePlace (lstPlaces["ID of place"] <==> lstPlaces[iFreePlace].
After that change the ID of free place (iFreePlace = "ID of place") and fresh lstMovableDraughts.

Name: 
In: 
Out: 
Description: 


