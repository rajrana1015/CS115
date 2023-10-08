'''
Created on 10/3/23
@author:   Raj Rana
Pledge:    I plegde that I have abided by the stevens Honor system.
CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here
def giveChange(amount,coins):
    """This function usese he timputs of an amoun and list of coin
denominations and returns he minimum number of coins and whose second
item is a list of the coins in that optimal solution"""
    if amount<=0:
        return [0,[]]
    if coins==[]:
        return [float("inf"),[]] 
    if amount<coins[0]:
        return giveChange(amount,coins[1:])
    else:
        used=giveChange(amount-coins[0],coins)
        useIt=[used[0]+1,used[1]+[coins[0]]]
        loseIt=giveChange(amount,coins[1:])
        return min(useIt,loseIt)

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#def wordScore(L,score):
#    if word==[]:
#        return []
#    elif L[0][0]==score[0][0]:
#        return score[0][1]
#    return wordScore(L[])
        
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

def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    """This funcation takes teh inpurst of the dictionary and scores, which
returns a list of list containing the word and its corresponding score"""
    if dct==[]:
        return []
    elif dct[0]=="":
        return [dct[0],0]
    else:
        return [[dct[0],wordScore(dct[0],scores)]]+wordsWithScore(dct[1:],scores)


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if L==[] or n==0:
        return []
    return [L[0]]+take(n-1,L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if L==[]:
        return []
    if n==0:
        return L
    else:
        return drop(n-1,L[1:])

