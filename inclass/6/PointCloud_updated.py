# PointCloud.py
""" Some basic operations on a cloud of points in
the plane are used to illustate various list-processing
basics."""

from random import randint as randi
from math import sqrt

def MakeCloud(n,max_coordinate):
    """ Returns lists of floats x and y that define a cloud
    of n points in the plane.
    
    The x and y values are randomly generated using the random.randint()
    in range 0 to max_coordinate.
    
    PreC: n is a positive integer greater than 1 and max_coordinate is a positive int.
    """
    # Build up x and y via repreated appending.
    x=[]
    y=[]
    for k in range(n):
        r = randi(0,max_coordinate)
        x.append(r)
        r = randi(0,max_coordinate)
        y.append(r)
    return (x,y)

def Diameter(x,y):
    """ Returns (d,imax,jmax) where d is a float that is the diameter of a cloud
    of points defined by lists x and y. imax and jmax are ints that are
    the indices of the diameter points.
    
    The diameter of a cloud of points is the maximum distance between any
    two points in the cloud. The two points for which this occurs are called
    diameter points. 
    
    PreC: x and y are lists of floats with the same length.
    """
    # d is the maximum separation between all pairs of points that have
    # so far been checked.
    d = 0.0
    n = len(x)
    all_distances = []
    
    
    for i in range(n):
        # Examine distances to the point (x[i],y[i])
        for j in range(n):
            dij = sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
            all_distances.append(dij)
            

            
            if dij>d:
                # The distance between the ith and jth points is
                # a new maximum. Update d and save the values of i and j.
                d = dij
                imax = i
                jmax = j
    return (d,imax,jmax, all_distances)

def ShowCloud(x,y):
    """ Displays a point cloud defined by x and y and highlights
    the two points  that define its diameter.
    
    PreC: x and y are lists of floats with the same length.
    """
    
    # Determine the indices of the points that define the diameter.
    all_distances = [] #list to track all computed distances returned from diameter function
    (d,i,j,all_distances) = Diameter(x,y)
    for k in range(len(x)):
        # Display the kth point in the cloud.
        if k==i or k==j:
            # This will highlight the diameter points.
            print("Diameter point: %d, %d" %(x[k],y[k]))
        else:
            print("Cloud point: %d, %d" %(x[k],y[k]))
    print('''Cloud end points: (%d, %d), (%d, %d).
          Cloud diameter = %6.2f.''' %(x[i],y[i], x[j],y[j], d))
    
    
    all_distances.sort() #ascending order
    print("all computef distances = ", all_distances)
    
   
# Application Script
if __name__ == '__main__':
    (x,y) = MakeCloud(10,10)
    ShowCloud(x,y)

