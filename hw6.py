'''
Created on 10/23/23
@author:   Raj Rana and Arin Ravindran
Pledge:    I plegde my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
from functools import reduce
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
numlist = []

def counter(S, a=1, n = None):
    """This function usse the imput of a string of 1's and 0's and
    returns a list of how many conceutive digits of that number there are"""
    if len(S) == 0:
        return []
    if n is None:
        n = S[0]
    if len(S) == 1:
        if n == S[0]:
            return [a]
        else:
            return [1]
    if S[0] == S[1]:
        return counter(S[1:], a + 1, n)
    else:
        return [a] + counter(S[1:], 1, S[1])
def dToB(num):
    """This function uses the input of an interger number and
    returns its binary form"""
    if num >= 1:
        return dToB(num // 2) + str((num % 2))
    else:
        return ''
def FivedToB(num):
    """This function uses ethe input of a binary number and
    returns it in a 5-bit binary form"""
    if num > 31:
        return  "1111100000" + FivedToB(num - 31)
    else:
        f = dToB(num)
        if len(f) < COMPRESSED_BLOCK_SIZE:
            return (('0' * (COMPRESSED_BLOCK_SIZE - len(f))) + f)
        else:
            return (('0' * (COMPRESSED_BLOCK_SIZE - len(f))) + f)
def compress(S):
    """THis function uses the input of a string of 1's and 0's and returns
    the 5-bit binary represention of the number of 1's and 0's in their respective order"""
    dlist = counter(S)
    if S[0] != '0':
        dlist = [0] + dlist
    return reduce(lambda x,y: x + '' + y, (map(FivedToB, dlist)))
""" In a comment, explain what is the largest number of bits that your
compress algorithm could possibly use to encode a 64-bit string/image.

The largest number of bits that the compressor fucntion will be 65 bits as
if  for the input binary string S is that it alternates between '0' and '1'
for all 64 bits, this would result in 64 5-bit binary represtions, but since
we must indeftify that the input string will begin  with a 1 and not a 0
then an additional 5-bit represtion of zero must be place infront of the
output, resulting in a total of 65 bits  """


def bToD(s):
    '''This function returns the integer corresponding to the binary representation in s.'''
    if s=="" or s=="0":
        return 0
    if s[-1]=="1":
        return 1+ 2*bToD(s[:-1])
    else:
        return 0+ 2*bToD(s[:-1])
def uncompressor(s,count):
    """This function uses the input of the 5-bit binary represention of the
    number of 1's and 0's in their respective order and return a string of
    its uncompressed verion"""
    if s=="":
        return ""
    if count%2==0:
        return "0"*bToD(s[:COMPRESSED_BLOCK_SIZE])+uncompressor(s[COMPRESSED_BLOCK_SIZE:],count+1)
    return "1"*bToD(s[:COMPRESSED_BLOCK_SIZE])+uncompressor(s[COMPRESSED_BLOCK_SIZE:],count+1) 
def uncompress(S,c=0):
    """This function uses the helper function uncompressor return a string of
    the uncompressed verion of S"""
    return uncompressor(S,0)

def compression(S):
    """return the ratio of the compressed size to the original size for
    image S."""
    return len(compress(S))/len(S)

def testCompression():
    """In a comment, describe the tests that you conducted and the compression
    ratios that you found.

    The three test conducted were to see the compression ratios on various 64
    bit binary image including a penguin, smile, and a five."""

    Penguin="00011000"+"00111100"*3 +"01111110"+"11111111"+"00111100"+"00100100"
    Smile="0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
    Five="1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
    zo="01"*32
    oz="10"*32
    assert compression(Penguin)==1.484375
    assert compression(Smile)==1.328125
    assert compression(Five)==1.015625
    assert compression(zo)==5.0
    assert compression(oz)==5.078125

"""In a comment, argue to NASA that Professor Lai is Lai-ing—such an algorithm cannot
exist! Try to make your reasoning as convincing and water-tight as possible. (In essence, you are
proving that such an algorithm cannot exist.)
Professors Lai's algortitim can not exist as the input and output would both be binary
strings that will result in a different out put when place in  the Laiuncompress function.
For example the image string of a pengunir is "00011000"+"00111100"*3 +"01111110"+"11111111"+"00111100"+"00100100"
or "0001100000111100001111000011110001111110111111110011110000100100" when uncrompressed, when it is compressed it will return 
"00011000100010100100001000010000100001000001100110000010100000010001000010000001000100000100010",
which is a much larger string. Since Lai's compressed will return the shorter of the two strings will return the orignal input
string, however this fail to acknowlegde the laiuncompress function will not be able to uncompress it correctly as it will return
the uncompressed verions or the original string but it will not be able to tell its already uncompssed thus reuturning an incorrect string.
For exmaple in our exmaple it would reutrn
"0000000000000000000000000000000001110000000000000000000000001111111111111110001111111111111111111111111111110000000000000000000000000000000
1111111111111111111111111111000000000000000000000000000000110000"
instead of "0001100000111100001111000011110001111110111111110011110000100100"
"""


