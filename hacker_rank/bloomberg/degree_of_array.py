def degreeOfArray(arr):
    freq = {}
    start = {}
    end = {}

    for i, num in enumerate(arr):
        freq[num] = 1 + freq.get(num, 0)
        if num not in start:
            start[num] = i
        end[num] = i

    max_freq = max(freq.values())
    result = 1e9
    for k, v in freq.items():
        if v == max_freq:
            result = min(result, end[k] - start[k] + 1)

    return result

# 5,1,2,2,3,1 => 2
# 6,1,1,2,1,2,2 => 4
print(degreeOfArray([5,1,2,2,3,1]))
print(degreeOfArray([6,1,1,2,1,2,2]))
