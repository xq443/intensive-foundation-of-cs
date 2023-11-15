# shapes.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Nov 10th, 2023

""" A framework to generate asterisks shapes, including left triangle, arrowhead, right triangle and boomerang.
    The input will be the menu choice and size, the output will be the designed asterisks shapes strings. """

def left_triangle (N):
    """
    Create a left triangle with specified size.

    Args:
       N(integer): representing the size of the left triangle 

    Returns:
        string: contains a left triangle of the specified size
    """
    result = "" #intialize the result shape string
    for i in range(1, N + 1):
        line = '*' * i #draw the asterisks shapes
        result += line.ljust(N)  # Left-align the line by padding with spaces
        if i < N:
            result += '\n' #the last line will not start a new line
    
    return result
    
    
def arrowhead(N):
    """
    Create an arrowhead with specified size.

    Args:
       N(integer): representing the size of the arrowhead 

    Returns:
        string: contains an arrowhead of the specified size
    """
    result = ""#intialize the result shape string
    # upper part
    for i in range(1, N):
        line = '*' * i   #draw the asterisks shapes
        result += line.ljust(N)  # Left-align the line by padding with spaces
        result += '\n'
    #lower part
    for i in range(N,0, -1):
        line = '*' * i    #draw the asterisks shapes
        result += line.ljust(N)  # Left-align the line by padding with spaces
        if i > 1:
            result += '\n'

    return result
    
def right_triangle(N):
    """
    Create a right triangle with specified size.

    Args:
       N(integer): representing the size of the right triangle 

    Returns:
        string: contains a right triangle of the specified size
    """
    result = "" #intialize the result shape string
    for i in range(N, 0, -1):
        line = '*' * i  #draw the asterisks shapes
        result += line.ljust(N)  # Left-align the line by padding with spaces
        if i > 1:
            result += '\n'
    
    return result
    
def boomerang(N):
    """
    Create a boomerang with specified size.

    Args:
       N(integer): representing the size of the boomerang

    Returns:
        string: contains a boomerang of the specified size
    """
    result = ""

    # Upper part of the boomerang
    for i in range(1, N + 1):
        line = '*' * i  #draw the asterisks shapes
        left_spaces = ' ' * (2 * (N - 1)  - 2 * (i - 1)) #draw the left part blanks
        right_spaces = ' ' * (i - 1)  #draw the right part blanks
        result += left_spaces + line + right_spaces + '\n' #concatenate left part blanks, asterisks shapes and right part blanks
        

    # Lower part of the boomerang
    for i in range(N - 1, 0, -1):
        line = '*' * i  #draw the asterisks shapes
        left_spaces = ' ' * (2 * (N - i)) #draw the left part blanks
        right_spaces = ' ' * (i -1)   #draw the right part blanks
        result += left_spaces + line + right_spaces #concatenate left part blanks, asterisks shapes and right part blanks
        if i > 1:
            result += '\n'

    return result     
    
if __name__ == '__main__':
    print("Let's draw some shapes together:")
    while True:
        try:
            print("0 - nothing(terminate program)")
            print("1 - left triangle")
            print("2 - arrowhead")
            print("3 - right triangle")
            print("4 - boomerang"); 
            R = input('Enter choice: ') #user input
            try: 
                R = int(R) #cast integer, if cannot case, the type of input is another type, proceed to exception error message
            except:
                print("\nInvalid choice, try again\n") # Exclude the float and string type
                continue

            if R == 0: #terminate the program
                print("\nThank you for drawing shapes with me!\n")
                break
                
            elif R in [1,2,3,4]:
                while True:
                    try:
                        N = int(input("Enter size (>= 3): ")) #cast integer, if cannot case, the type of input is another type, proceed to exception error message
                    except ValueError:
                        print("\nSize should be a positive integer!")  # Exclude the string and float type
                    else:
                        try:
                            if N >= 3:
                                #call the functions to draw shapes correspondingly
                                if R == 1:
                                    shape = left_triangle(N)
                                elif R == 2:
                                    shape = arrowhead(N)
                                elif R == 3:
                                    shape = right_triangle(N)
                                elif R == 4:
                                    shape = boomerang(N)
                                print("\n" + shape + "\n")
                                break
                            else:
                                raise ValueError("\nSize should be a positive integer!")
                        except ValueError as e: 
                            print(e)    
            else:
                raise ValueError("\nInvalid choice, try again\n") # Exclude cases that are not in [0,4]
        except ValueError as e:
            print(e)

