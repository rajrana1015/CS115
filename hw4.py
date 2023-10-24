'''
Created on 10/13/23
@author:   Raj Rana
Pledge: I plegde that I have abided by the Stevens Honor System.
CS115 - Hw 4
'''
def pas_help(n,r):
    """This function uses the input of the number of the row(n)
and the index of that row(r) and returns a new list of sums of
adjacent terms in the original list."""
    if n==r or r==0:
        return 1
    else:
        return pas_help(n-1,r-1)+pas_help(n-1,r)

def pascal_row(n,count=0,row=[]):
    """This function uses the input of the number of the row(n),
the count of which index the funciton is calling(which is 0 by default),
and the index in the sequence(row), which will return the sequence of
numbers for that row in pascals triangle."""
    if count>n:
        return row
    else:
        return pascal_row(n,count+1,row+[pas_help(n,count)])
def pascal_triangle(n,count=0,row=[]):
    """This funciton uses the input of the number of the row(n), and returns
all the sequences from row 0 till the nth row. """
    if count>n:
        return row
    else:
        return pascal_triangle(n-1)+[pascal_row(n)]
def test_pascal_row():
    """This funciton test the function pascal_row by asserting the function
with an input and expected output"""
    assert pascal_row(0)==[1]
    assert pascal_row(3)==[1, 3, 3, 1]
    assert pascal_row(6)==[1, 6, 15, 20, 15, 6, 1]
    assert pascal_row(8)==[1, 8, 28, 56, 70, 56, 28, 8, 1]

def test_pascal_triangle():
    """This funciton test the function pascal_triangle by asserting the function
with an input and expected output"""
    assert pascal_triangle(0)==[[1]]
    assert pascal_triangle(6)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1,6,15,20,15,6,1]]
    assert pascal_triangle(5)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(3)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(1)==[[1], [1, 1]]
