# Siri.py
# Name: Xujia Qin
# Email: qin.xuj@northeastern.edu
# Date: Oct 13th, 2023
""" This program is to convert a route string into a sequence of driving instructions. """
""" The input will be the English char letter (NWES) combinations,
    and the output will be several lines, including the original starter and intersection strings,
    starter string, as well as the intersection instruction strings.

    Noted here, i add up the validation part, if there is invalid input character occurring, the program will end, and only proceed the valid parts before

    For example, EKEE will deliver: EKEE
                                    Start Driving East
                                    Invalid Intersection String
                 AEEE will deliver  Invalid direction input, character must be one of NESW."""

""" This function will take two intersection strings as input and produce the appropriate intersection
    instruction string as return"""
def SiriSez(I):
    if I == 'EN': #cases when it's supppose to turn left
        result =  'Turn Left'
    elif I == 'NW':
        result =  'Turn Left'
    elif I == 'WS':
        result =  'Turn Left'
    elif I == 'SE':
        result =  'Turn Left'
    elif I == 'ES':#cases when it's supppose to turn right
        result =  'Turn Right'
    elif I == 'SW':
        result =  'Turn Right'
    elif I == 'WN':
        result =  'Turn Right'
    elif I == 'NE':
        result =  'Turn Right'
    elif I == 'WW':#cases when it's supppose to continue straight
        result =  'Continue Straight'
    elif I == 'SS':
        result =  'Continue Straight'
    elif I == 'NN':
        result =  'Continue Straight'
    elif I == 'EE':
        result =  'Continue Straight'
    elif I == 'SN':#cases when it's supppose to make a u-turn
        result =  'Make a U-Turn'
    elif I == 'NS':
        result =  'Make a U-Turn'
    elif I == 'WE':
        result =  'Make a U-Turn'
    elif I == 'EW':
        result =  'Make a U-Turn'
    else: # cases that the input is not NEWS combination
        raise ValueError("Invalid Intersection String") # we raise the ValueError with the error message
    return result

"""This function takes a valid route string and prints seven lines of output:
Line 1 The route string.
Line 2. The associated starter string.
Lines 3-7. The associated intersection instruction strings."""

def TripAdvisor(Route):
    if not is_valid_direction(Route[0]):#check if the first inpur char is valid, if not valid, the program will end and print corresponding error message
        print("Invalid direction input, character must be one of NESW.")
    else: #if the first char is valid
  
        #print route string
        print(Route)

        #interpret the first char input
        if(Route[0] == 'N'):
            print('Start Driving North')
        elif(Route[0] == 'S'):
            print('Start Driving South')
        elif(Route[0] == 'E'):
            print('Start Driving East')
        elif(Route[0] == 'W'):
            print('Start Driving West')
                

        #take each two chars as input of SiriSez function to deliver intersection instruction string    
        for j in range(0,len(Route)- 1): #considering the boundary check, the last loop will stop when i = len(Route) - 2 
            instruction = Route[j:j+2] #using index slice to deliver the two chars representing direction instruction we gonna consider
            try:
                res = SiriSez(instruction)
                print(res)
            except ValueError as e: #here the exception connects with SiriSez function's raise ValueError statement,
                #after first char validation, if the following chars are invalid, we use break to end the program and print the error message
                print(e)
                break
            
            
"""This function is to valid the input, if all chars are from "NESW", we can proceed to TripAdvisor(Route),
   otherwise the program will print error message and let the user retype the input"""
def is_valid_direction(char):
    return char in "NSEW" #return character that are from "NESW"
    
# Application Script
if __name__ == '__main__':
    I = input('Enter an Intersection String: ').strip() #if there are quotes in the first and last index of the input, we use index slicing to remove them.
  
    Result = TripAdvisor(I) #recall TripAdvisor function
    
