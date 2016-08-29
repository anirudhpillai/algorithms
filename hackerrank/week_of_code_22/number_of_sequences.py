# A sequence of n integers is nice if the following conditions are satisfied:
# You're given a sequence, A1 to An, where some numbers may be -1.
# Find and print the number of nice sequences you can create
# by changing each -1 to a non-negative integer.
# As this number can be quite large, your answer must be modulo 10^9 + 7.

n = int(input())
seq = list(map(int, input().split()))

def getFactors(x):
    ret = []
    for i in range(1, x):
        if x % i == 0:
            ret.append(i)
    return ret

def getTotal(arr):
    try:
        m = arr.index(-1) + 1
    except:
        return 1

    factors = getFactors(m)
    total = 0
    #try replacing -1 with everything possible
    for i in range(m):
        check = True
        for k in factors:
            if arr[k-1] != i % k:
                check = False
                break
        if check:
            arr[m-1] = i
            total += getTotal(arr)
            arr[m-1] = -1
    return total

print(getTotal(seq))
