import math


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """

        len_of_dimension = minutesToTest // minutesToDie + 1
        return int(math.ceil(math.log(buckets, len_of_dimension)))

# StefanPochmann
# https://discuss.leetcode.com/topic/67666/another-explanation-and-solution/2

# def poorPigs(buckets, minutesToDie, minutesToTest):
#     pigs = 0
#     while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
#         pigs += 1
#     return pigs
