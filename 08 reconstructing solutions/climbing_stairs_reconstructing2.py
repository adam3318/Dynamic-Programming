"""
    Problem:
        Find the minimum cost path to reach the nth stair only taking k steps
        return index locations in the path

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
        f(n) = minimun( f(n-1) + f(n-2) 


    Order of execution:
        bottom-up
    
    Where to look for the answer:
        f(n)
"""

"""
Time complexity: o(n)
    loop through n data and doing constant work each time
Space complexity: o(n)
    allocated n number of variables
"""

def climbing_stairs(n:int, k:int, price:[]) -> [int]:
    
    ways = [0] * (n+1) # array of size k
    ways[0] = 0
    #ways[1] = price[1]
    minimum = 999 # max int here
    from_array = [0] * (n+1)

    for i in range(1,n+1):
        for j in range(1,k+1): 
            if (i-j) < 0:
                 continue
        
            if ways[i-j] + price[i] < minimum:
                  from_array[i] = i-j
                  minimum = ways[(i-j)] + price[i]
                  ways[i] = ways[(i-j)] + price[i]
                  
        minimum = 999
            
    curr = n
    reconstructed_path = []
    while(curr > 0):
        reconstructed_path.append(curr)
        curr = from_array[curr]
          
    reconstructed_path.append(0)
    reconstructed_path.reverse()
    return reconstructed_path
    
prices = [0,3,2,4,1,5,1,7,1]
print(climbing_stairs(8,2, prices)) #5

prices = [0,3,2,4]
print(climbing_stairs(3,2, prices)) #6

