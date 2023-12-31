'''
Unique Paths
A robot is located at the top-left corner of a m x n grid (marked
'S' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked
'E' in the diagram below).
How
many possible unique paths are there?

-----------------
| S |   |   |   | 
-----------------
|   |   |   |   | 
-----------------
|   |   |   | E | 
-----------------

Above is a 3 x 4 grid. How many possible unique paths are there?
'''
import numpy as np


def print_grid(symbol, x,y):
    print((x*4+1)*"-")
    for i in range(y):
        for j in range(x):
            print(f"|   ", end='')
        print("| ")
        print((x*4+1)*"-")
#print_grid('0', 4,3)
        

def unique_path(m: int, n: int) -> int:
    #twoD_list = np.zeros((m,n),dtype=int)
    twoD_list = [ [0] * n for i in range(m)]
    twoD_list[0][0] = 1
    
    for i in range(m):
        for j in range(n):

            if i > 0 and j > 0:
                twoD_list[i][j]= twoD_list[i-1][j] + twoD_list[i][j-1]
            elif i > 0:
                twoD_list[i][j] = twoD_list[i-1][j]
            elif j > 0:
                twoD_list[i][j] = twoD_list[i][j-1]

    print(type(twoD_list))
    
    return twoD_list[i][j]

print( unique_path(3,4) )

