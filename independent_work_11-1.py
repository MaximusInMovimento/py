def fib(n):
    a, b = 1, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


g = fib(200)
lst = list(g)
print(lst[len(lst)-1])
