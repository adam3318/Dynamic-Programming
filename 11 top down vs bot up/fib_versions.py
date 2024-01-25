
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(4))

class fib_memoized():

    def __init__(self) -> None:
        self.cache = {0:0,1:1}
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib( n-1) + self.fib( n-2)
        return self.cache[n]
    

print(fib_memoized().fib(5))


        
        