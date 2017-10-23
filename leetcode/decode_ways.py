class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        memo = [1] + [0 for _ in range(len(s))]

        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                memo[i] += memo[i-1]
            if i != 1 and 10 <= int(s[i-2:i]) <= 26:
                memo[i] += memo[i-2]

        return memo[-1]
