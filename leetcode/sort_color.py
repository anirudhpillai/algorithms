class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def partition(num, j):
            for i in range(j, len(nums)):
                if nums[i] == num:
                    if nums[j] != num:
                        nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            return j

        j = partition(0, 0)
        j = partition(1, j)
        j = partition(2, j)
