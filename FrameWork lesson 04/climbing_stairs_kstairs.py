"""
    Problem:
        Find the number of ways to reach the nth stair while only taking k steps

    Framework for Solving DP Problems:
        1. Define the objective function
        2. Identify base cases
        3. Write down a recurrence relation for the optimized objective function
        4. What's the order of execution?
        5. Where to look for the answer?

    Objective function:
        f(i) is the total number of ways to get to the ith step 

    Idenify base cases:
        f(0) = 1
        f(1) = 1
        f(2) = 2

    Recurrence relation: 
        f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(n-k)

    Order of execution:
        bottom-up
    
    Where to look for the answer:
        f(n)
"""

"""
Time complexity: o(n)
    loop through n data and doing constant work each time
Space complexity: o(1)
    allocated constant number of variables
"""

def climbing_stairs(n:int, k:int):
    
    ways = [0] * k

    ways[0] = 1
    

    for i in range(1,n+1):
        #f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(n-k) is a for loop as seen below:
        for j in range(1,k):
            if (i - j < 0):
                continue
            ways[i % k] += ways[(i-j) % k]

    return ways[i % k]

print(climbing_stairs(6,2))