class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        half = None

        if len(nums) % 2 == 0:
            half = len(nums) // 2
        else:
            half = (len(nums) // 2) + 1

        less, greater = (nums[:half])[::-1], (nums[half:])[::-1]
        l, g = 0, 0

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = less[l]
                l += 1
            else:
                nums[i] = greater[g]
                g += 1
