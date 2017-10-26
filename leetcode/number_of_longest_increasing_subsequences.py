class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        memo = [[1, 0] for _ in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i][0] = max(memo[i][0], memo[j][0] + 1)
            for j in range(i):
                if nums[i] > nums[j] and memo[j][0] == memo[i][0] - 1:
                    memo[i][1] += memo[j][1]
            memo[i][1] = max(memo[i][1], 1)

        longest = max([i[0] for i in memo])
        return sum([i[1] for i in memo if i[0] == longest])
