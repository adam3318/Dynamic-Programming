"""
    Problem:
        Find the number of ways to reach the nth stair while only taking 1 or 2 steps

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

    Recurrence relation: 
        f(n) = f(n-1) + f(n-2)

    Order of execution:
        bottom-up
    
    Where to look for the answer:
        f(n)
"""

"""
Time complexity: o(n)
    loop through n data and doing constant work each time
Space complexity: o(n)
    allocate an array of size n
"""
    
def climbing_stairs(n:int):
    
    ways = [None] * (n+1)

    ways[0] = 1
    ways[1] = 1

    for i in range(2,n):
        ways[i] = ways[i-1] + ways[i-2]

    return ways[i]

print(climbing_stairs(6))

    