# DiceRollsSol.py
# Name: Xujia Qin
# Nov 1st, 2023
""" List computations and for-loops."""

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
    """ Roll 3 die many times and record the outcomes
    using lists. Then pose some questions of the stored data.
    """
    N = 100000
    D1 = randiList(1,6,N)
    D2 = randiList(1,6,N)
    D3 = randiList(1,6,N)
    # Set up a list  D where D[k] is the value when three dice are rolled
    D = []
    for k in range(N):
        ThreeThrows = D1[k] + D2[k] + D3[k]
        D.append(ThreeThrows)
        
    #TODO 1: Assign to a variable ave0 the average value in D.
    ave0=0.0 #place holder declaration
    
    # Calculate the sum of all values in the list D
    total = 0
    for value in D:
        total += value

    # Calculate the average value by dividing the sum by the total number of values
    ave0 = float(total) /float(N)
    print ('Average when 3 die are rolled = %6.4f' % ave0)
        
    #TODO 2: Assign to a variable Prob1 an estimate of the probability
    # that the sum of the three die values is 7.
    Prob1=0.0 #place holder declaration
    
    # Count the number of times the sum is 7
    counter = 0
    for value in D:
        if value == 7:
            counter += 1
    # Estimate the probability by dividing the count by the total number of trials N
    Prob1 = float(counter)/float(N)
    print  ('Prob1 = %6.4f' % Prob1)
    
    #TODO 3: Assign to a variable Prob2 an estimate of the probability
    # that one die value is at least as big as the sum of the other
    # two die values
    Prob2=0.0   #place holder declaration
    
    # Count the number of times one die value is at least as big as the sum of the other two die values
    counter_1 = 0
    for k in range(N):
        if (D1[k] >= D2[k] + D3[k]) or (D2[k] >= D1[k] + D3[k]) or (D3[k] >= D1[k] + D2[k]):
            counter_1 += 1
    # Estimate the probability by dividing the count by the total number of trials N
    Prob2 = float(counter_1) /float(N) 
    print  ('Prob2 = %6.4f' % Prob2)
    





