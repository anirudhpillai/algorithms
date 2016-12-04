def fib():
    x, y = 1, 2
    while x < 4000000:
        if not x % 2:
            yield x
        x, y = y, x+y

print(sum(fib()))
