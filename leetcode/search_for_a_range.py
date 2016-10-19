"""
Given a sorted array of integers, find the starting and ending
position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""



class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def find(find_left):

            low, high = 0, len(nums)-1
            result = -1

            while low <= high:
                mid = (high + low)/2
                if nums[mid] == target:
                    result = mid
                    if find_left:
                        high = mid-1
                    else:
                        low = mid+1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return result

        return [find(True), find(False)]
