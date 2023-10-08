############################################################
# Name:Raj Rana
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
# CS115 HW 1
#
############################################################
from functools import reduce
"""THe function below(mult) is create to be used an appliable function
when reducing in the funciton factorial, this allows for the last step
of the fomula which is multiplying all the numbers in the list."""
def mult(x,y):
    return x*y
"""The function factoral uses the mult function to muiltiple the values
fromt he list that is created for the formula when and input is given.
The range function allows for all the number before the input to be save
in a list"""
def factorial(n):
    return reduce(mult,range(1,n+1))
"""The function add will sum the given inputs from a list and return it"""
def add(x,y):
    return(x+y)
"""The function mean will use add to sum all of the values in a a list
using the reduce function and then use the len fucntion to find the number
of values in a list aloowing it to divide by the sum thus resutling in the
mean of the list"""
def mean(L):
    return (reduce(add,L))/len(L)
    
