# be greedy
class Solution(object):
    def minPatches(self, nums, n):
        miss = 1
        patched = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss = miss + nums[i]
                i += 1
            else:
                miss += miss
                patched += 1

        return patched


""" My first attempt
Should have been improved by looking at the algorithm inside
the algorithm. The algorithm of the solution above was all that
was necessary to solve the problem

from itertools import combinations


def minPatches(nums, n):
    reached = [0 for _ in range(n)]

    for i in range(1, len(nums)+1):
        for j in combinations(nums, i):
            print(j)
            s = sum(j)-1
            if s < len(reached):
                reached[s] = 1

    print(reached)

    def update_reached(num):
        indx = [i for i in range(len(reached)) if reached[i] == 1]
        for i in indx:
            if i+num < len(reached):
                reached[i+num] = 1
        reached[num-1] = 1
    patched = 0

    def add_patch():
        for i in range(len(reached)):
            if reached[i] == 0:
                print("adding patch: " + str(i+1))
                update_reached(i+1)
                return

    while not all(map(lambda x: x == 1, reached)):
        add_patch()
        print(reached)
        patched += 1

    return patched

print(minPatches([1, 5, 10], 20))
"""
