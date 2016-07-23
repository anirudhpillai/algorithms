def give(arr, i, choc):
    for j in range(len(arr)):
        if j is not i:
            arr[j] += choc
    return arr

def check(arr):
    return all(map(lambda m: m is arr[0], arr))

def answer(arr):
    if check(arr):
        return 0
    ret = 1000
    for i in range(len(arr)):
        temp = min(answer(give(arr, i, 1)),
                answer(give(arr, i, 2)),
                answer(give(arr, i, 5)))
        ret = min(temp, ret)
    return ret

print(answer([2,2,3]))
