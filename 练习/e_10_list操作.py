def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
for var in fib(20):
    print(var)


