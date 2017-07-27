import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        result = list(self.nums)

        for i in range(len(result)):
            j = random.randint(0, i)
            result[i], result[j] = result[j], result[i]

        return result
