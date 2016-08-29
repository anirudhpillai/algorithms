# Consider two n-element multisets (i.e., unordered and
# possibly containing duplicate elements) of integers,
# You can perform the following operation on set X:
# Choose two elements at some postions Xi and Xj where 0<=i, j<n and i != j.
# Decrement Xi by 1 and increment Xj by 1.
# Given X and Y, find and print the
# minimum number of operations you must perform so that X is equal to Y
# (i.e., both sets contain the same exact values,
# and the order doesn't matter); if such a thing is not possible,
# print instead.

n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X.sort()
Y.sort()

diff = [X[i] - Y[i] for i in range(n)]

if sum(diff) != 0:
    print(-1)
else:
   print(sum([i for i in diff if i > 0]))

# the following solution is when they are arrays and not sets

# n = int(input())
# X = list(map(int, input().split()))
# Y = list(map(int, input().split()))
#
# diff = [X[i] - Y[i] for i in range(n)]
#
# if sum(diff) != 0:
#     print(-1)
# else:
#     sum_so_far = 0
#     check = True
#     for i in diff:
#         sum_so_far += i
#         if sum_so_far < 0:
#             print(-1)
#             check = False
#             break
#     if check:
#         print(sum([i for i in diff if i > 0]))
