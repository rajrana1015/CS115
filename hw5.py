'''
Created on 10/16/23
@author:   Raj Rana
Pledge: I plegde my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''
lucas_seq={}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in lucas_seq:
        return lucas_seq[n]
    if n==0:
        lucas_seq[n]=2
        return lucas_seq[n]
    elif n==1:
        lucas_seq[n]=1
        return lucas_seq[n]
    else:
        lucas_seq[n]=fast_lucas(n-1)+fast_lucas(n-2)
        return lucas_seq[n]
change={}
def fast_change(amount,coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    
    if (amount,tuple(coins)) in change:
        return change[amount,tuple(coins)]
    if amount==0:
        change[amount,tuple(coins)]=0
        return change[amount,tuple(coins)]
    if coins==[]:
        change[amount,tuple(coins)]=float("inf")
        return change[amount,tuple(coins)]
    elif coins[0]>amount:
        change[amount,tuple(coins)]=fast_change(amount, coins[1:])
        return change[amount,tuple(coins)]
    else:
        useIt=1+fast_change(amount-coins[0],coins[0:])
        loseIt=fast_change(amount,coins[1:])
        change[amount,tuple(coins)]= min(useIt,loseIt)
        return change[amount,tuple(coins)]
# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


