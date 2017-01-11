class Solution(object):
    def minMoves(self, nums):
        #  return sum(i-min(nums) for i in nums)
        return sum(nums) - len(nums)*min(nums)
