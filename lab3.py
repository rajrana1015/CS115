'''
Created on 9/28/23
@author:Raj Rana
Pledge: I plegde that I have abided by the Stevens Honor System.
CS115 - Lab3
'''
def change(amount,coin):
    """The funciton change uses the input of an amount
and checks wether the amount is able to be dirstiubted
in the coin denominations, if not then it returns 0 and
if the denominations are not present it returns infinty.
if both are avaible, then the fucnito uses the use_it or
lose_it method to create variousions of  the amount of coins need
to create the amount and then returns the verion that uses the lowest
amount."""
    if amount==0:
        return 0
    if coin==[]:
        return float("inf")
    elif coin[0]>amount:
        return change(amount, coin[1:])
    else:
        useIt=1+change(amount-coin[0],coin[0:])
        loseIt=change(amount,coin[1:])
        return min(useIt,loseIt)
    
