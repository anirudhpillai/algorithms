class Solution:
    def maxCoins(self, input):
        """
        https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
        """
        # left and right boundaries fixed at 1
        # remove 0s
        nums = [1] + [i for i in input if i > 0] + [1]
        dp = [[0 for _ in nums] for _ in nums]

        for k in range(2, len(nums)):
            for left in range(0, len(nums) - k):
                right = left + k
                for i in range(left + 1, right):
                    # assume i is the last balloon to be burst
                    # 1 and 1 added at boundaries
                    # so don't need to worry about that
                    dp[left][right] = max(
                        dp[left][right], (
                            nums[left] * nums[i] * nums[right]
                            + dp[left][i]
                            + dp[i][right]
                        )
                    )

        return dp[0][len(nums)-1]
