class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         j = i+1
        #         while j < len(nums):
        #             if nums[j] != 0:
        #                 nums[i], nums[j] = nums[j], nums[i]
        #                 break
        #             j += 1

        # m = -1
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         if m == -1 or nums[m] != 0:
        #             m = i
        #     elif m != -1:
        #         nums[i], nums[m] = nums[m], nums[i]
        #         m += 1

        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[j] == 0:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
