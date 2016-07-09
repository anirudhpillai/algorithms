# Original solution but can do better

def solve(arr):
    sum = 0
    for i in range(len(arr)):
        temp = []
        for j in range(i, len(arr)):
            temp.append(arr[j] - arr[i])
        sum += max(temp)
    return sum

print(max_profit([1,2,100]))
