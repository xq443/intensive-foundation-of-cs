# ShowSimpleMath.py

""" Module contains a script that uses the built-in
module math and the user-written module SimpleMath.

It compares the accuracy of the SimpleMath functions sqrt,
cos, and sin with their counterparts in the math module"""
    
import math 
import SimpleMath

# Check out the square root function
x = float(input(' Compute the square root of x = '))
MySqrt = SimpleMath.sqrt(x)
TrueSqrt = math.sqrt(x)
print ('SimpleMath.sqrt(x) = '+str(MySqrt)+'\n      math.sqrt(x) = '+str(TrueSqrt)+' \n' )
#print ('SimpleMath.sqrt(x) = %12.8f\n      math.sqrt(x) = %12.8f \n' % (MySqrt,TrueSqrt))

theta = float(input('theta (degrees) = '))
theta = (math.pi*theta)/180
MyCos = SimpleMath.cos(theta)
TrueCos = math.cos(theta)
MySin = SimpleMath.sin(theta)
TrueSin = math.sin(theta)

print ('SimpleMath.cos(theta) = '+str(round(MyCos,8))+'\n      math.cos(theta) = ' + str(round(TrueCos,8)) )
print ('SimpleMath.sin(theta) = '+str(MySin)+'\n      math.sin(theta) = ' + str(TrueSin) )

#print ('SimpleMath.cos(theta) = %12.8f\n      math.cos(theta) = %12.8f ' % (MyCos,TrueCos))
#print ('SimpleMath.sin(theta) = %12.8f\n      math.sin(theta) = %12.8f ' % (MySin,TrueSin))

r = float(input(' Enter the radiu of a circle  = '))
s1 = SimpleMath.pi * r**2

s2 = math.pi * r**2
print ('SimpleMath the area of a circle with radiu 100 = ' + str(s1) + '\n math the area of a circle with radiu 100 = ' + str(s2))




    
