"""
    Problem:
        Find the sum of the first N numbers.

    Objective function:
        f(i) is the sum of the first i elements.

    Recurrence relation: 
        f(n) = f(n-1) + n

        keep in mind:
            if n = 1 then the recurrence relation fails bc f(0) doesnt exist therefore this must be initialized beforehand
"""

def nSum(n: int):
    if  type(n) != int or n < 0:
        return None

    dp_sum = [None] * (n + 1)
    dp_sum[0] = 0
    

    
    for i in range(1,n+1):
        dp_sum[i] = dp_sum[i-1] + i

    return dp_sum[n]



