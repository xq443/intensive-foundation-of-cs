# ShowInput.py
""" Illustrates the input function."""

x = input('Enter a float like 5.1: ')
y = float(x)/3
print (x,y)

x = input('Enter an int like 8: ')
y = int(x)/3
print (x,y)

x = input('Enter a number in quotes like \'-5.2\': ')
y = x+x
print (x,y)

x = input('Enter a general string like \'abc\': ')
y = x+x
print (x,y)

x = input('Enter a string without quotes like abc: ')
y = x+x
print (x,y)

"""
Summary...

1. If you respond to an input prompt with a decimal
number, it will return a float.

2. If you respond to an input prompt with a single-quoted string,
it will return a string.

"""











