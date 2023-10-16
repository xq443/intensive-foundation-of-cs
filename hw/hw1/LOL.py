# LOL.py
# Name: Xujia Qin
# Email id: qin.xuj@northeastern.edu
# Sept. 26th, 2023
""" Explores how long it takes you to enter a given random length-3 string."""
"""The input will be the random string generated, the output will be the result of checking if the test string is the same as the usr input string, and the elapsed time calculated"""

from datetime import datetime
from random import choice

# S1 is the random test string
# S2 is the response string
# t1 is the first timestamp string
# t2 is the second timestamp string

# Generate a random test string of length 3
alfa = 'abcdefghijklmnopqrstuvwxyz' # you can make the challenge easier by deleting characters
S1 = choice(alfa) + choice(alfa) + choice(alfa) # concatenate the three random characters generated

# Prompt the user to start the test
input('Press the return key when you are ready')

# # First time stamp
t1 = datetime.utcnow()

# Display the test string
print('The test string:', S1)

# Prompt the user to enter their response
S2 = input('Enter the test string as fast as you can: ')

# Second time stamp
t2 = datetime.utcnow()

# Calculate elapsed time in seconds
elapsed_time = (t2 - t1).total_seconds()

# Check user's response
if S2 == S1:
    print('Correct response') # if the response is exactly the same as the test string
elif len(S2) == 3: # if the response is length-3 but does not agree with the test string
    print('There is a character mismatch in your response')
else: # if the esponse is not a length-3 string.
    print('Your response has the wrong number of characters')
    
# Print elapsed time with three decimal places
print('Elapsed Time = {:.3f} seconds'.format(elapsed_time))
print ('\n' + str(t1) + '\n' + str(t2))

