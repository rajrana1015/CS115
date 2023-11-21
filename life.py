#
# life.py - Game of Life lab
#
# Name: Raj Rana
# Pledge: I plegde my honor that I have abided by the Stevens Honor System.
#

import sys, random
def createOneRow(width):
    """ returns one row of zeros of width "width"...
    You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A
def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
def innerCells(w,h):
    """This function uses the input of the  width and
    hieght of the 2D array craeted and outputs an array
    in which all inner cells are 1's and all outer calls
    are 0's"""
    A = createBoard( w, h )
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = 1
    return A
def randomCells(w,h):
    """This function uses the input of the  width and
    hieght of the 2D array craeted and outputs an array
    in which all inner cells are randomly chooses to be
    either a 1 or 0 and all outer calls are 0's"""
    A = createBoard( w, h )
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = random.choice([0,1])
    return A
def copy(A):
    """Thia function uses the input of a 2D array and
    outputs an array a identical copy of the array"""
    height = len(A)
    width = len(A[0])
    newA = createBoard(height,width)
    for row in range(height):
        for col in range(width):
            newA[row][col]=A[row][col]
    return newA
def innerReverse(A):
    """This function uses the input of a 2D array and
    outputs an reversed copy array in which the inner
    cells that are 1 turn into 0 and the inner calls
    that are 0 turn into 1, and all outercells are 0"""
    A3=copy(A)
    for row in range(1,len(A3)-1):
        for col in range(1,len(A3[0])-1):
            if A3[row][col]==0:
                A3[row][col]=1
            elif A3[row][col]==1:
                A3[row][col]=0
    return A3
def countNeighbors(row,col,A):
    """This function uses the inputs of the current
    cell's row column and array name, then it counts
    and returns how many cells in the current cells
    surrounding is a 1"""
    count=0
    for j in [-1,0,1]:
        for i in [-1,0,1]:
            if i==0 and j==0:
                continue
            if A[row+j][col+i]==0:
                count+=0
            if A[row+j][col+i]==1:
                count+=1
    return count
def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    A3=copy(A)
    for row in range(1,len(A3)-1):
        for col in range(1,len(A3[0])-1):
            if A3[row][col]==0 and countNeighbors(row,col,A)==3:
                A3[row][col]=1
            elif A3[row][col]==1 and countNeighbors(row,col,A)>3:
                A3[row][col]=0
            elif A3[row][col]==1 and countNeighbors(row,col,A)<2:
                A3[row][col]=0
            else:
                continue
    return A3
