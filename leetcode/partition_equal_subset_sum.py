class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        """ Top Down Memoised Fastest
        memo = {}

        def helper(curr_ind, accumulated):
            if (curr_ind, accumulated) in memo:
                return memo[(curr_ind, accumulated)]

            if accumulated > target:
                return False
            if accumulated == target:
                return True

            for i in range(curr_ind, len(nums)):
                if helper(i+1, accumulated + nums[i]):
                    memo[(curr_ind, accumulated)] = True
                    return True

            memo[(curr_ind, accumulated)] = False
            return False

        return helper(0, 0)
        """

        # This is a 0/1 Knapsack problem

        """ Bottom up with O(n*target) space
        dp = [[False for _ in range(target + 1)] for _ in nums]

        for i in range(len(nums)):
            if 0 <= nums[i] <= target:
                dp[i][nums[i]] = True
            for j in range(target+1):
                if i > 0 and dp[i-1][j]:
                    dp[i][j] = True

                    if nums[i] + j == target:
                        return True
                    elif nums[i] + j < target:
                        dp[i][nums[i] + j] = True

        return dp[len(nums)-1][target]
        """

        # Bottom up O(2*target) space
        dp = [True] + [False for _ in range(target)]

        for i in range(len(nums)):
            temp = []
            for j in range(target+1):
                if dp[j] and nums[i] + j <= target:
                    temp.append(nums[i] + j)

            for i in temp:
                dp[i] = True

        return dp[target]
