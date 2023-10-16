# Golden.py
# Name: Xujia Qin
# Date: Sept.26th, 2023
# Email id: qin.xuj@northeastern.edu

"""Using Fibonacci equation and Lucas number equation to display fn , rn, and Ln, n + 1, fn+1, and rn+1, and Ln+1 given the input (positive integer) n where n <= 35 """
"""The output data type: n(integer), fn and f(n+1) will be integers, rn and r(n+1) will be float rounded with 15 digits, Ln and L(n+1) will be integers"""
from math import *

# Function to calculate the nth Fibonacci number
def fibonacci(n):
    fn = (1 / sqrt(5)) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) # using the the n-th Fibonacci number equation given in the question 
    return fn
    

# Function to calculate the nth Lucas number
def lucas(n):
    Ln = 2 * fibonacci(n + 1) - fibonacci(n) # using Ln = 2Fn+1 – Fn to derive the nth lucas number
    return Ln


# Function to calculate the golden ratio
def golden_ratio(n):
    rn = fibonacci(n + 1) / fibonacci(n) # using rn = f(n+1)/f(n) equation
    return rn

# Get input from the user
n = int(input("Enter a positive integer (n ≤ 35): "))

# Check if n is within the valid range
if n <= 35:
    # express the six variables using functions we defined above
    fn = fibonacci(n)
    rn = golden_ratio(n)
    Ln = lucas(n)

    fn_plus_1 = fibonacci(n + 1)
    rn_plus_1 = golden_ratio(n + 1)
    Ln_plus_1 = lucas(n + 1)

    # Initilize the first and second row tuple
    data_displayed_first_row = (n,fn,rn,Ln)
    data_displayed_second_row = (n+1, fn_plus_1, rn_plus_1, Ln_plus_1)

    # Set the specified format with proper character width and decimal digits by left-align
    format_specification = '%-5d %-10d %-18.15f %-8d'

    # Display the result table in a formatted specification
    print (format_specification % data_displayed_first_row)
    print (format_specification % data_displayed_second_row)
else:
    print("Invalid input. n should be less than or equal to 35.") # if n is not within the valid range, we gonna print the error message
