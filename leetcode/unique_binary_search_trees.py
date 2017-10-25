class Solution(object):
    def __init__(self):
        self.memo = {0: 1}

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n not in self.memo:
            result = 0
            for i in range(1, n+1):
                result += self.numTrees(i-1) * self.numTrees(n-i)
            self.memo[n] = result

        return self.memo[n]
