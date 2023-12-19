

def climbing_stairs(n:int, k: int, prices:[int]) -> int:
    ways = [0] * k
    minimum = 999 # max int goes here

    for i in range(1,n+1):
        
        for j in range(k): #find minimum value between k-1, k-2, ...
            if (i - j) < 0:
                continue
            
            next_value = ways[(i-j) % k]

            if next_value < minimum:
                minimum = next_value
                

        ways[i%k] = minimum + prices[i]
        minimum = 999
        

    return ways[n%k]

prices = [0,3,2,4,1,5,1,7,1]
print(climbing_stairs(8,2, prices))

prices = [0,3,2,4]
print(climbing_stairs(3,2, prices))