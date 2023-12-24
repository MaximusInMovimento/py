def fib(n):
    a, b = 1, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


f = open("fibonachhi", "w")
for i, val in enumerate(fib(200)):
    f.write(f"{i+1} : {val}\n")
f.close()
