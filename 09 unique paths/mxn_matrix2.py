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
|   | 1 | 1 | 1 | 
-----------------
|   |   |   | E | 
-----------------

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Above is a 3 x 4 grid. How many possible unique paths are there?
'''
import numpy as np
import random
#from sys import maxint

def print_grid(symbol, x,y):
    print((x*4+1)*"-")
    for i in range(y):
        for j in range(x):
            print(f"|   ", end='')
        print("| ")
        print((x*4+1)*"-")
#print_grid('0', 4,3)
        
def create_grid_with_obstacles(m: int, n: int) -> np.ndarray:
    twoD_list = np.zeros( (m,n) , dtype=int)
    for i in range(min(m,n)-1):
        twoD_list[random.randint(1, m-1)][random.randint(1, n-1)] = -1 #(-maxint -1)
    
    return twoD_list
    


def unique_path_with_obstacles(array: np.ndarray) -> int:
    twoD_list = array
    twoD_list[0][0] = 1
    m = array.shape[0]
    n = array.shape[1]

    for i in range(m):
        for j in range(n):
            if twoD_list[i][j] == -1: #(-maxint -1):
                twoD_list[i][j] = 0
                continue
            if i > 0 and j > 0:
                twoD_list[i][j]= twoD_list[i-1][j] + twoD_list[i][j-1]
            elif i > 0:
                twoD_list[i][j] = twoD_list[i-1][j]
            elif j > 0:
                twoD_list[i][j] = twoD_list[i][j-1]

    
    
    return twoD_list[i][j]

arry = create_grid_with_obstacles(3,4)
print(arry)
y = unique_path_with_obstacles(arry)
print(f"There are {y} ways to get from the top left to the bottom right while avoiding the obstacles")

