from random import randint as randi

x = 0
y = 0
T = ""
L = 5
nSteps = 0 #initialize the counter variable
while abs(x) < L and abs(y) < L:
    r = randi(1,4)
    if(r == 1):
        y = y+1
        T = T + "N"
    elif(r == 2):
        x = x+1
        T = T + "E"
    elif(r == 3):
        y = y -1
        T = T + "S"
    else:
        x = -1
        T = T + "W"
    nSteps = nSteps + 1 #increment nSteps by 1 after moving one step
    


# Calculate the final position based on the counts of each direction
final_x = T.count('E') - T.count('W')
final_y = T.count('N') - T.count('S')

print("x-y coordinates of the robot’s final position: x =", final_x, ", y =", final_y)
