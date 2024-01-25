"""
Problem:
Paint Fence With Two Colors
There is a fence with n posts, each post can be painted with either green or blue color.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.
"""

import numpy as np

def color_fence(n,number_of_colors):
    c = number_of_colors
    twoD_list = np.zeros( (n + 1,c) , dtype=int)
    
    #green = 1
    #blue = 0

    twoD_list[1][0] = 1
    twoD_list[1][1] = 1
    twoD_list[2][0] = 2
    twoD_list[2][1] = 2
    

    for i in range(3,n+1):
        for j in range(c):
            twoD_list[i][j] = twoD_list[i-1][1-j] + twoD_list[i-2][1-j]
    print(twoD_list)
    return twoD_list[n,1] + twoD_list[n,0]
    

y = color_fence(5,2)
print(y)
