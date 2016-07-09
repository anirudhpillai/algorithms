# similar to coin_change.py but there order has to be unique
# here all the possible sequences are needed

import math

def solve(N):
    if N < 1:
        return 0
    if N is 1:
        return 1
    if N is 4:
        return 2
    return solve(N-1) + solve(N-4)

def primes_less_than(n):
    if n < 2:
        return 0
    tot = 1
    for num in range(3, n+1, 2):
        if all(num%i is not 0 for i in range(2, int(math.sqrt(num))+1)):
            tot += 1
    return tot

def answer(N):
    return primes_less_than(solve(N))

print(primes_less_than(30))
