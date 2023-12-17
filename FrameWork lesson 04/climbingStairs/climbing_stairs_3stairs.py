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
        f(2) = 2

    Recurrence relation: 
        f(n) = f(n-1) + f(n-2) + f(n-3)

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
    
def climbing_stairs(n:int):
    if n < 2: return 1
    if n == 2: return 2

    a = 1
    b = 1
    c = 2
    answer = None

    for i in range(3,n+1):
        answer = a + b + c
        a = b
        b = c 
        c = answer

    return answer

print(climbing_stairs(5))