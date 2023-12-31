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
        
def create_grid(m: int, n: int) -> np.ndarray:
    twoD_list = np.zeros( (m,n) , dtype=int)
    for i in range(m):
        for j in range(n):
            twoD_list[i][j] = random.randint(1, 100)
    
    return twoD_list
    


def unique_path_max_profit(array: np.ndarray) -> int:
    twoD_list = array
    
    m = array.shape[0]
    n = array.shape[1]
    from_array = np.empty([m, n], dtype=np.ndarray)
    

    for i in range(m):
        for j in range(n):
            if twoD_list[i][j] == -1: #(-maxint -1):
                twoD_list[i][j] = 0
                continue
            if i > 0 and j > 0:
                if twoD_list[i-1][j] > twoD_list[i][j-1]:
                    twoD_list[i][j] += twoD_list[i-1][j]
                    from_array[i][j] = [i-1,j]
                else:
                    twoD_list[i][j] += twoD_list[i][j-1]
                    from_array[i][j] = [i,j-1]

                #twoD_list[i][j] += max(twoD_list[i-1][j], twoD_list[i][j-1]) # += is the same as adding price at current index
                #from_array[i][j] = max()
            elif i > 0:
                twoD_list[i][j] += twoD_list[i-1][j]
                from_array[i][j] = [i-1,j]
            elif j > 0:
                twoD_list[i][j] += twoD_list[i][j-1]
                from_array[i][j] = [i,j-1]
    
    #curr = [m,n]
    curr = [m-1,n-1]
    reconstructed_path = []
    while(curr[0]> 0 or curr[1] > 0):
        reconstructed_path.append(curr)
        curr = from_array[curr[0]][curr[1]]
          
    reconstructed_path.append([0,0])
    reconstructed_path.reverse()
    return reconstructed_path, twoD_list[i][j]
    
    #return twoD_list[i][j]

arry = create_grid(3,4)
print(arry)

profit = unique_path_max_profit(arry)[1]
path = unique_path_max_profit(arry)[0]
print(f"The maximum profit is {profit}")
print(f"The unique path of maximum profit is: {path}")

