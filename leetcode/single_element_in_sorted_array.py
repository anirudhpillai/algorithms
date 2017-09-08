class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, high = 0, len(nums) // 2

        while lo < high:
            mid = (lo + high) // 2
            if nums[mid*2] != nums[mid*2 + 1]:
                high = mid
            else:
                lo = mid + 1

        return nums[lo*2]
