class Solution(object):
    def removeElement(self, nums, val):
        """
        Similar to Remove Duplicates from Sorted Array
        """
        tail = 0
        for i, k in enumerate(nums):
            if k != val:
                nums[tail] = k
                tail += 1
        return tail
