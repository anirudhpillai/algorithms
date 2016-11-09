"""
Given an array nums containing n + 1 integers where each integer
is between 1 and n (inclusive). Find duplicate number
Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array,
but it could be repeated more than once.
"""


# can't modify the array so can't change the number nums[nums[i]]
# to negative and wait for overlap
# so using the below method based on binary search


class Solution(object):
    def findDuplicate(self, nums):
        low = 1
        high = len(nums)-1

        while low < high:
            mid = (high+low)/2
            count = len([i for i in nums if i <= mid])
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low
