# Count2DiceRolls.py
""" Elementary examples that demonstrate the
use of lists of numbers."""

from random import randint as randi

def randiList(L,R,n):
    """ Returns a length-n list of
    random integers from interval [L,R]
    
    PreC: L,R,n ints with L<=R and n>=1
    """
    x = []
    for k in range(n):
        r = randi(L,R)
        x.append(r) 
    return x

if __name__ == '__main__':
    """ Rolls a pair of dice many times and displays the outcome.
    """
    N = 10000
    D1 = randiList(1,6,N)
    D2 = randiList(1,6,N)
    # Set up a list  D where D[k] is the outcome of the k-th rolling
    # of the dice pair...
    D = []
    for k in range(N):
        TwoThrows = D1[k] + D2[k]
        D.append(TwoThrows)
    # Count how many of each possible outcome
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for k in range(N):
        i = D[k]
        count[i] = count[i]+1
    # Display results...
    print ('\n Roll a pair of dice %1d times.' % N)
    print ('\nk  count[k]   prob  ')
    print ('-----------------')
    for k in range(2,13):
       #print ('  %2d  %6d  %6d' % (k,count[k]))
        print (" " + str(k) + "    " + str(count[k]) + "    "+ str(float(count[k] / N)))








