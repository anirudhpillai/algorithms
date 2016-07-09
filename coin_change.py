def count(arr, change):
    table = [0] * (change+1)
    table[0] = 1
    for i in arr:
        for j in range(i, change+1):
            table[j] += table[j - i]
    return table[change]

print(count([2,5,3,6], 10))
