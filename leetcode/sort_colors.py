# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         def partition(num, j):
#             for i in range(j, len(nums)):
#                 if nums[i] == num:
#                     if nums[j] != num:
#                         nums[j], nums[i] = nums[i], nums[j]
#                     j += 1
#             return j
#
#         j = partition(0, 0)
#         j = partition(1, j)
#         j = partition(2, j)


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def partition(start, end):
            pivot = nums[end]
            border = start
            for i in range(start, end+1):
                if nums[i] <= pivot:
                    nums[border], nums[i] = nums[i], nums[border]
                    if i != end:
                        border += 1
            return border

        def quicksort(start, end):
            if end <= start:
                return
            p = partition(start, end)
            quicksort(start, p-1)
            quicksort(p+1, end)

        quicksort(0, len(nums) - 1)
