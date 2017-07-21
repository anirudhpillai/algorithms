class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}

        for i, k in enumerate(nums):
            if target - k in mp:
                return [mp[target-k], i]
            else:
                mp[k] = i
