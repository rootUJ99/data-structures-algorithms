def fib(n):
    if n < 2: return 1
    else: return fib(n-1) + fib(n-2)


mem = {}
def fibmem(n):
    if n in mem:
        return mem[n]
    else:
        f = 0
        if n < 2: 
            f = 1
        else: 
            f = fib(n-1) + fib(n-2)
            mem[n] = f
            return f

print(fib(10))
print(fibmem(10), mem)
