def caching_fibonacci():
    cache = {}
    cacheCalls = 0

    def fibonacci(n):
        if n <= 0: 
            return 0
        elif n == 1:
            return 1
        elif cache.get(n):
            print(f'Using cache for {n}')
            return cache.get(n)
        
        cache[n] = fibonacci(n-1) + fibonacci(n - 2)
        return cache.get(n)
    
    return fibonacci

fibo = caching_fibonacci()

for n in range(50, 1, -1):
    print(f"N = {n}; Fibonacci = " + str(fibo(n)))
        