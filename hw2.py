'''
Created on 9/27/23
@author:   Raj Rana
Pledge: I plegde that I have abided by the Stevens Honor System.
CS115 - Hw 2
'''
import sys
from functools import reduce
# Be sure to submit as hw2.py.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def letterScore(letter,scorelist):
    """This function uses the input of a letter and check if that letter matches
the a key in the scrabble scores list and returns the corersponing value."""
    if letter==[]:
        return []
    elif letter==scorelist[0][0]:
        return scorelist[0][1]
    return letterScore(letter,scorelist[1:])

def wordScore(word,scorelist):
    """This function usese input of a word, to the input each letter of the word
into the letterScore fucntion to return the values of each letter and add them up."""

    if word=="":
        return 0
    return letterScore(word[0],scorelist)+wordScore(word[1:],scorelist)

def inRack(Rack,charater):
    """This functions checks wether  the frist letter of the term is in the Rack and
returns a 1 or -1 whcih allows makeWord to either make a word with the charater or move
on to the next one."""
    if charater in Rack:
        if Rack[0]== charater:
            return 0
        return 1+inRack(Rack[1:],charater)
    else:
        return -1

def makeWord(Rack, term):
    """This function returns a word that can made by they letters given in the Rack."""
    if term=="":
        return True
    if inRack(Rack,term[0])==-1:
        return False
    Nrack = Rack[0:inRack(Rack,term[0])]
    Nrack = Nrack + Rack[inRack(Rack,term[0])+1:len(Rack)]
    return makeWord(Nrack,term[1:])

def inDic(Rack,n):
    """This function uses the makeWord function and wordScore function to return a
list of words from dictionary that can be made from the letters in Rack."""
    if n+1>len(Dictionary):
        return[]
    if makeWord(Rack,Dictionary[n]):
        return[[Dictionary[n]]+[wordScore(Dictionary[n],scrabbleScores)]]+inDic(Rack,n+1)
    else:
        return inDic(Rack,n+1)

def scoreList(Rack):
    """Uses the helper functions inDic, makeWord and inRack each of them calling itself
and the one after it respectivly inorder to return a list of list containing words that
can be made from the rack without using duplicate amounf of letters."""
    return inDic(Rack,0)

def bigN(x,y):
    """This functions takse the input x and y, checks and returns the varible with the
greater value(score)."""
    if x[1]>y[1]:
        return x
    elif y[1]>x[1]:
        return y
    else:
        return x + y

def bestWord(Rack):
    """This function uses the bigN function to reduce the list from scorelist by returning the word that has the greatest value."""
    if scoreList(Rack)==[]:
        return ['',0]
    return list(reduce(bigN,scoreList(Rack)))
