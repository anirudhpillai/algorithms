class Solution(object):
    def increasingTriplet(self, nums):

        # dp = [1 for _ in nums]

        # for i in range(len(nums)):
        #     for j in range(i-1, -1, -1):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return True if [i for i in dp if i >= 3] else False

        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
