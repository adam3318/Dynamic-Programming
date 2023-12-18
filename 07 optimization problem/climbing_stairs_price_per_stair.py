"""
    Problem:
        Find the minimum cost to reach the nth stair only taking k steps

    Framework for Solving DP Problems:
        1. Define the objective function
        2. Identify base cases
        3. Write down a recurrence relation for the optimized objective function
        4. What's the order of execution?
        5. Where to look for the answer?

    Objective function:
        f(i) is the total number of ways to get to the kth step 

    Idenify base cases:
        f(0) = 1

        notes:
            everything else is calculated iteratively 

    Recurrence relation: 
        f(n) = minimun( f(n-1) + f(n-2) + f(n-3) + ... + f(n-k))

        notes:
            this screams for loop!... for k in range(1,k+1) BUT if tabulated array is of size k
            change the for loop to: for k in range(1,k) because when "overwriting memoory" use 
            addition to that index therefore no need to include + f(n-k)
                e.g. 
                k = 2 
                dp[2,3] and the next fib number is 5 therefore add 3 to 2 and the operation is 
                complete. This operation is synonmous to f(5) = f(5-1) + f(5-2) where f(5-1) is 3
                and f(5-2) is the 2 at index 0. 

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

def climbing_stairs(n:int, k:int, price:[]) -> int:
    
    ways = [0] * (n+1) # array of size k
    ways[0] = 0
    for i in range(1,n+1):
            ways[i] = min(ways[(i-1)] , ways[i-2]) + price[i]
            
        

    return ways[i]

prices = [0,3,2,4,1,5,1,7,1]
print(climbing_stairs(8,2, prices))

prices = [0,3,2,4]
print(climbing_stairs(3,2, prices))