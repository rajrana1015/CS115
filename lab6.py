'''
Created on 10/19/23
@author:   Raj Rana
Pledge:    I plegde my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2==0:
        return False
    else:
        return True

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''

    """Q1: base-2 respresention of 42: 101010"""

    """Q2: Given an odd base-10 number, least-significant bit - the rightmost bit -
    in its base-2 representation will be a 1 as 2^0 will result in a 1 which is
    needed to create a odd number as any number in the x of 2^x will only result
    in a even value. In the same sense if you have a even number you wont need a
    value in the right most place value as it will result in a odd value."""

    """Q3:If the least-significant bit is removed from a base-2 number, the original
    number will be halved, as 1010(10) will become 101(5)"""

    """Q4:Finding base-2 represention of N:
    -When N is odd for Y is denoted by N/2, 1 should be added at the end of Y's binary
    version since dividing a odd number by 2 will result in a decimal/float, thus rounding down to the nearest int
    - When N is even for Y is denoted by N/2, 0 should be added at the end of Y's binary
    version since dividing a odd number by 2 will not result in a remainder."""
    if n==0:
        return ""
    if isOdd(n):
        return numToBinary(n//2)+"1"
    else:
        return numToBinary(n//2)+"0"
def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=="" or s=="0":
        return 0
    if s[-1]=="1":
        return 1+ 2*binaryToNum(s[:-1])
    else:
        return 0+ 2*binaryToNum(s[:-1])
def increment(s):
    '''Precondition: s is a string of 8 bisits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    n=binaryToNum(s)
    if len(numToBinary(n+1))>8:
        return "00000000"
    return (8-len(numToBinary(n+1)))*"0" + numToBinary(n+1)
def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n>=0:
        print(s)
        return count(increment(s),n-1)
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    """Q5: To return the value of 59 as a ternary value we must divide 59 by 3
    3,with result value being the next ternary vlaue left and the first ternianry value bring the result of n%3"""
    if n==0:
        return ""
    else:
        return numToTernary(n//3) +str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=="" or s=="0":
        return 0
    return int(s[0])*(3**(len(s)-1)) + ternaryToNum(s[1:])
