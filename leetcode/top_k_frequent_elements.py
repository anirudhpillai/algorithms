# using hash table and bucket sort
# def top_k(nums, k):
#     # count the frequency for each element
#     table = dict()
#     for i in nums:
#         if i in table:
#             table[i] += 1
#         else:
#             table[i] = 1
#
#     # get the max frequency
#     maximum = max(table.values())
#
#     # initialize an array of arrays, index is frequency,
#     # value is list of numbers
#     arr = [[] for i in range(maximum+1)]
#
#     for number, count in table.items():
#         arr[count].append(number)
#
#     result = []
#
#     for i in range(maximum, 0, -1):
#         for a in arr[i]:
#             result.append(a)
#
#         if len(result) == k:
#             break
#
#     return result

# using heap
from queue import PriorityQueue

def top_k(nums, k):
    table = dict()
    for i in nums:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1

    Q = PriorityQueue()
    for num, freq in table.items():
        Q.put((freq, num))
        if Q.qsize() > k:
            Q.get()

    result = []
    while Q.qsize():
        result.append(Q.get()[1])

    return list(reversed(result))

print(top_k([1,1,1,2,2,3], 2))
