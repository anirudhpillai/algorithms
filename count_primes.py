class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        prime = [True for _ in range(n)]
        count = 0

        for i in range(2, n):
            if prime[i]:
                count += 1
                j = 2
                while i * j < n:
                    prime[i*j] = False
                    j += 1

        return count
