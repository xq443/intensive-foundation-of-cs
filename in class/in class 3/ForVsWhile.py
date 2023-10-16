# ForVsWhile.py
""" Looks at while-loop solutions and for-loop solutions that
are equivalent.
"""

print ('\nThe first 5 positive integers via a for-loop:\n')
for k in range(1,6):
    print ('k = %3d' % k)

print ('\nThe first 5 positive integers via a while-loop:\n')
k = 1
while(k<=5):
    print ('k = %3d' % k)
    k = k+1
    
print ('\nThe first 5 odd positive integers via a for-loop:\n')
for k in range(1,10,2):
    print ('k = %3d' % k)

print ('\nThe first 5 oddpositive integers via a while-loop:\n')
k = 1
while(k<=10):
    print ('k = %3d' % k)
    k = k+2
    
print ('\nThe first 5 positive integers via a for-loop:\n')
for k in range(5,0,-1):
    print ('k = %3d' % k)

print ('\nThe first 5 positive integers via a while-loop:\n')
k = 5
while(k>0):
    print ('k = %3d' % k)
    k = k-1
    
print ('\nCount from 100 down to 30 in steps of -10 via a for-loop:\n')
for k in range(100,20,-10):
    print ('k = %3d' % k)

print ('\nCount from 100 down to 30 in steps of -10 via a while-loop:\n')
k = 100
while(k>=30):
    print ('k = %3d' % k)
    k = k-10

print ('\nThe first 5 even positive integers via a for-loop:\n')
#TODO: write your code here
for k in range(1, 11):
    if(k % 2 ==0):
        print ('k = %3d' % k)

for k in range(1,6):
    print ('k = %3d' % (k * 2))
    

print ('\nThe first 5 even positive integers via a while-loop:\n')
#TODO: write your code here
count = 0
k = 1
while(count < 5):
    if(k % 2 ==0):
        print ('k = %3d' % k)
        count += 1
    k += 1
        

k = 1
while(k <6):
    print ('k = %3d' % (k * 2))
    k += 1
    
