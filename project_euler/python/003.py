plist = [2]


def primes(max):
    for i in range(3, max, 2):
        for p in plist:
            if i % p == 0 or p*p > i:
                break
            if i % p:
                plist.append(i)
                yield i


def factors(number):
    for prime in primes(number):
        if number % prime == 0:
            number /= prime
            yield prime
        if number == 1:
            break

print(max(factors(8)))
print(max(factors(600851475143)))
