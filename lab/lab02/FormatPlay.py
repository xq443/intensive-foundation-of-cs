# FormatPlay.py
""" A short script that illustrates formatted print."""

from math import pi
x = 355
y = 113
z = float(x)/float(y)
err = abs(z - pi)
print('\nNumerator   Denominator   Quotient      Error')
print('-----------------------------------------------')
print(str(x).rjust(6) + str(y).rjust(11) + str(round(z,7)).rjust(18) + str(round(err,9)).rjust(13))



print '%6d %10d %17.7f %12.2e' % (x,y,z,err)

