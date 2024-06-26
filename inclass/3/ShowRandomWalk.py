# ShowRandomWalk.py
""" Estimates the average number of hops required
for the robot to reach the boundary."""

from random import randint as randi

def RandomWalk(L):
    """
    Returns the number of steps required to comple a random walk
    in one dimension.
  
    Simulates a one-dimensional  random walk that continues until
    the absolute value of the x-coordinate of the robot
    equals L. 
  
    Precondition: L is a positive int.
    """
    # Initialize the hop counter and the current location
    hops = 0; x = 0
    while abs(x) < L:
        r = randi(0,1)
        if r==0:
           x += 1
        else:
           x -= 1
        hops += 1
    return hops


def AveRandomWalk(L,n):
    """
    Retruns the Average number of hops required to complete random walk on a length-L
    runway. n is the number of trials.
  
    Precondition: L and n are positive ints.
    """
    s = 0   # Running sum
    for k in range(0,n):
         s += RandomWalk(L)
    return float(s)/float(n)
 
#Demo Script 
if __name__ == '__main__':
    # Report the average number of hops required
    # to complete the random walk for L = 5,10,15,...,40.
    n = 500  # Number of trials
    print ('\nL   = Length of the runway')
    print ('Ave = Average number of hops required to complete the walk\n')
    print ('   L      Ave ')
    print ('--------------')
    for L in range(1,51):
        print ('  %2d   %6.1f' %(L,AveRandomWalk(L,n)))
    print ('\n Averages based on %1d trials.\n' %n)
        
    
    
    






