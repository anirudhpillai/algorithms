"""
Reservoir Sampling
http://www.geeksforgeeks.org/reservoir-sampling/
"""

import random


class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        result = -1

        for i, num in enumerate(self.nums):
            if num == target:
                # Here reservoir has only 1 place therefore checking if 0
                if random.randint(0, count) == 0:
                    result = i
                count += 1

        return result
