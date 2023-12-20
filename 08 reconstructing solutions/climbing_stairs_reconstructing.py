

def climbing_stairs(n:int, k:int, price:[]) -> [int]:
    
    ways = [0] * (n+1) # array of size k
    ways[0] = 0
    ways[1] = price[1]
    from_array = [0] * (n+1)

    for i in range(2,n+1):
            ways[i] = min(ways[(i-1)] , ways[i-2]) + price[i]
            
            if ways[i-1] < ways[i-2]:
                  from_array[i] = i-1
            else:
                  from_array[i] = i-2
                  
        
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

