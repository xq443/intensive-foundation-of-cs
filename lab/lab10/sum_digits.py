#sum_digits.py

def sum_digits(n):
    """ Returns the sum of the digits of n
       
    Recursive implementation
    
    PreC: n is a positive integer.
    """
    # if it is a single digit, return it as the sum
    if n < 10:
        return n
    else: #if the number of digits >= 2
        #base case as considering the last digit
        base = n % 10 
        sum_curr = sum_digits(n // 10) # shrink cases that sum the remaining digits exclude the last digit
        return base + sum_curr #add up the last digit and the remaining digits

    
if __name__ == '__main__':

    num = int(input("Enter a positive integer: "))

    if num<0:
        print("The number should be greater than 0.")
        exit(0)
    sum_of_digits = sum_digits(num)
    print("Sum of digits in the number %d = %d " %(num, sum_of_digits))
