from math import gcd


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        if z <= 0 or x == z or y == z or x + y == z:
            return True
        return z % gcd(x, y) == 0


# Can also be done using bfs but that's slower
# https://discuss.leetcode.com/topic/50425/breadth-first-search-with-explanation/2
