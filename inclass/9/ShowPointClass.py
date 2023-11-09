# ShowPointClass.py
""" Illustrate the class  Point
"""

from ThePointClass import *

def ShowPoint(P):
    print('(%3.3f, %3.3f)' %(P.x , P.y))
    
    
def Midpoint(P1,P2):
    """ Returns a point that is the midpoint of
    a line segment that connects P1 and P2.
    
    PreC: P1 and P2 are points.
    """
    xm = (P1.x+P2.x)/2.0
    ym = (P1.y+P2.y)/2.0
    Q = Point(xm,ym)
    return Q

def RandomPoint(Lx,Rx,Ly,Ry):
    """ Returns a point that is randomly chosen
    randomly from the square Lx<=x<=Rx, Ly<=y<=Ry.
    
    PreC: L and R are floats with L<R
    """
    x = randu(Lx,Rx)
    y = randu(Ly,Ry)
    P = Point(x,y)
    return P

if __name__ == '__main__':
    """ demonstrates all the methods in the Point class
    and some functions that manipulate Point objects.
    """
    
        
    # Create and display two points...
    P = Point(1,2)
    print("Point P: ")
    ShowPoint(P)
    Q = Point(-2,-2)
    print("Point Q: ")
    ShowPoint(Q)
    
    # Indicate the distance between them...
    d = P.Dist(Q)
    
    
    # Compute and display the midpoint
    M = Midpoint(P,Q)
    print("Next, showing midpoint. ")
    ShowPoint(M)

    
    # Reflect the red point...
    S = P.Reflect()
    print("Reflection of point P: ")
    ShowPoint(S)
    
    
    # Display ten random points...
    for k in range(10):
        P = RandomPoint(1,2,-2,-1)
        print("Random point %d" %k)
        ShowPoint(P)
        
    print(M.Dist(P))
    print(M.Dist(Q))
    
    


