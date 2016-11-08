class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        (s_1, s_2, ..., s_n) is a divisible subset sorted in increasing order,
        so s_n is a multiple of s1, s1, ...,s_{n-1},
        if s_{n+1} is larger than s_n and is a multiple of s_n,
        then (s_1, s_2, s_3, ..., s_n, s_{n+1}) is also a divisible subset.
        """

        if not nums:
            return []

        nums.sort()

        s = []

        for i in range(0, len(nums)):
            ms = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    ms = max(ms, s[j], key=lambda x: len(x))

            s.append(ms + [nums[i]])

        return max(s, key=lambda x: len(x))
