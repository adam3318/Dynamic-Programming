"""
Unique Paths
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.
The goal is to obtain the max profit from the grid of numbers.

-----------------
| 1 | 2 | 3 | 4 | 
-----------------
| 6 | 5 | 2 | 1 | 
-----------------
| 7 | 11| 20| 1 | 
-----------------

It is obvious that the path is to go all the way down then all the way right. But for all cases?

"""


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
    for i in range(m):
        for j in range(n):
            twoD_list[i][j] = random.randint(1, 100)
    
    return twoD_list
    


def unique_path_max_profit(array: np.ndarray) -> int:
    twoD_list = array
    
    m = array.shape[0]
    n = array.shape[1]

    for i in range(m):
        for j in range(n):
            if twoD_list[i][j] == -1: #(-maxint -1):
                twoD_list[i][j] = 0
                continue
            if i > 0 and j > 0:
                twoD_list[i][j] += max(twoD_list[i-1][j], twoD_list[i][j-1]) 
            elif i > 0:
                twoD_list[i][j] += twoD_list[i-1][j]
            elif j > 0:
                twoD_list[i][j] += twoD_list[i][j-1]

    
    
    return twoD_list[i][j]

arry = create_grid_with_obstacles(3,4)
print(arry)
y = unique_path_max_profit(arry)
print(f"The maximum profit is {y}")

