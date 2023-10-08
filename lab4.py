'''
Created on 10/5/23
@author:   Raj Rana
Pledge:    I plegde that I have abided by the stevens Honor system.
CS115 - Hw 3
'''
def knapsack(cap,item):
    """This function use the inputs of a capacity and
list of list coniaintg the weight and value of an item and
returns a list with the maxium value of item able to be carried and a list
of each item's weight and value."""
    if cap<=0:
        return [0,[]]
    if item==[]:
        return [0,[]] 
    if cap<item[0][0]:
        return knapsack(cap,item[1:])
    else:
        use=knapsack(cap-item[0][0],item[1:])
        use1=use[0]+item[0][1]
        useIt=[use1,[item[0]]+use[1]]
        loseIt=knapsack(cap,item[1:])
        if useIt[0]>loseIt[0]:
            return useIt
        else:
            return loseIt
