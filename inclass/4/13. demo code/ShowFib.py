# ShowFib.py
"""
while-loop investigations of the Fibonacci sequence and its relation
to the golden ration = (1+sqrt(5))/2.

Background:
Given a "current" Fibonacci number and its "predecessor",
the "next" Fibonacci number is the sum of the current
and the predecessor. Starting off with a 0 and 1 as
the predeecessor and the current  Fibonacci number, we get

               0,1,1,2,3,5,8,13,21,34, etc
               
We index the Fibonacci numbers by where they are in this
sequence, e.g.,

             0 is the zeroth Fibonacci number
            13 is the seventh Fibonaccis number
            34 is the nineth Fibonacci number
            
"""
import math

#Problem 1. Print out Fibonacci numbers 1 through 15

# Initializations
k = 1
x = 0  # the past Fibonacci number
y = 1  # the current Fibonacci number
z = 1  # the next Fibonacci number
ratio = float(z)/float(y)
# y is the k-th Fibonacci number
print ('\n  k     kth Fib      kth Ratio ')
print ('--------------------------------------')
while k<=15:
    print ('%3d %10d     %14.12f' %(k,y,ratio))
    k += 1
    x = y       #  Fib k-1
    y = z       #  Fib k
    z = x+y     #  Fib k+1
    ratio = float(z)/float(y)
    
#Problem 2. Print out Fibonacci numbers
# 1 through k where k is the first Fibonacci
# number whose ratio is < .000001

# Initializations
r = (1 + math.sqrt(5))/2
k = 1
x = 0  # the past Fibonacci number
y = 1  # the current Fibonacci number
z = 1  # the next Fibonacci number
# y is the k-th Fibonacci number
error = abs(float(z)/float(y)-r)
print ('\n  k     kth Fib    kth Ratio Error ')
print ('--------------------------------------')
while error>=.000000001:
    print ('%3d %10d     %14.12f  ' %(k,y,error))
    k += 1
    x = y       #  Fib k-1
    y = z       #  Fib k
    z = x+y     #  Fib k+1
    error = abs(float(z)/float(y)-r)
print ('%3d %10d     %14.12f  ' %(k,y,error))
    

#Problem 3. Print out the smallest Fibonacci
# number bigger than 1000000

# Initializations
k = 1
x = 0  # the past Fibonacci number
y = 1  # the current Fibonacci number
z = 1  # the next Fibonacci number
# y is the k-th Fibonacci number
while y<1000000:
    k += 1
    x = y       #  Fib k-1
    y = z       #  Fib k
    z = x+y     #  Fib k+1
print ('\nThe smallest Fibonacci number > million is Fib %1d =  %1d' % (k,y))

#Problem 4. Print out the largest Fibonacci
# number less than 1000000

# Initializations
k = 1
x = 0  # the past Fibonacci number
y = 1  # the current Fibonacci number
z = 1  # the next Fibonacci number
# y is the k-th Fibonacci number
while z<1000000:
    k += 1
    x = y       #  Fib k-1
    y = z       #  Fib k
    z = x+y     #  Fib k+1
print ('\nThe largest  Fibonacci number < million is Fib %1d =  %1d' % (k,y))


#Problem 5. Ask user to enter an int value N. Print the N-th Fibonacci number
#E.g., if the user enters 7, print 13; if the user enters 9, print 34, etc. 


n = int(input("PLease enter an int value n: "))
# Initializations
k = 1
x = 0  # the past Fibonacci number
y = 1  # the current Fibonacci number: the kth FN
z = 1  # the next Fibonacci number
# y is the k-th Fibonacci number
while k < n:
    k += 1
    x = y       #  Fib k-1
    y = z       #  Fib k
    z = x+y     #  Fib k+1
    print("The " + str(k) + "-Nth  Fibonacci number is " + str(y))
    
print ('\nThe ' + str(n) +"-Nth  Fibonacci number is " + str(y))



