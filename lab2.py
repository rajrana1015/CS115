###########################################################
# Name: Raj Rana
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#
############################################################

"""This function uses hte inputs of L and K to produce a dot product by
multiplying ht efirs tindex od L to the first index of K and then add its
product to the product of the second index of L and the second index of K."""
def dot(L,K):
    if L==[] or K==[]:
        return 0
    return (L[0]*K[0])+ dot(L[1:],K[1:])

"""This function uses the input s and returns each singluar letter of
the input in a list via indexing"""
def explode(S):
    if S=="":
        return []
    return [S[0]]+ explode(S[1:])

"""This function uses the element, e, and a list, L, and returns the
index at the point where the element e is equal in value to a value in
the list L"""
def ind(e,L):
    if L==[] or L=="" or L[0]==e:
        return 0
    return 1+ind(e,L[1:])

"""This function uses the eelement, e, and the list, L, and returns a
new list that does not hav eht eelement e as a value int he list by
returning the next non-e-item if a value of e is found in the list. """
def removeAll(e,L):
    if L==[]:
        return []
    elif e==L[0]:
        return removeAll(e,L[1:])
    return [L[0]]+ removeAll(e,L[1:])

"""The funciton below uses the function, x, and the list, L, and
returns a list in which all vlaues of x(y) returns true"""
def myFilter(x,y):
    if y==[]:
        return []
    elif x(y[0])==False:
        return myFilter(x,y[1:])
    else:
        return [y[0]]+ myFilter(x,y[1:])

"""This function uses the input list, n, and returns a reverse version
of the list regardless if a nested list is present by running the fuction
on the list if the idex of the outer list is read as a list"""
def deepReverse(n):
    if n==[]:
        return []
    elif isinstance(n[-1],list):
        return [deepReverse(n[-1])] + deepReverse(n[:-1])
    else:
        return[n[-1]]+deepReverse(n[:-1])

