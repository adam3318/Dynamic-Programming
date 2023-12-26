def climbing_stairs(n:int, k:int, price:[]) -> [int]:
    
    ways = [0] * (k+1) # array of size k
    ways[0] = 0
    #ways[1] = price[1]
    minimum = 999 # max int here
    from_array = [0] * (n+1)

    for i in range(1,n+1):
        for j in range(1,k+1): 
            if (i-j) < 0:
                 continue
        
            if ways[(i-j) % k] + price[i] < minimum:
                  from_array[i] = i-j
                  minimum = ways[(i-j) % k] + price[i]
                  
        ways[i % k] = minimum
        minimum = 999 # max int
            
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