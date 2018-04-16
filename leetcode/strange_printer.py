class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}

        def helper(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            if start > end:
                return 0

            result = 1 + helper(start + 1, end)

            for k in range(start+1, end+1):
                if s[start] == s[k]:
                    result = min(
                        result,
                        helper(start, k-1) + helper(k+1, end)
                    )

            memo[(start, end)] = result
            return result

        return helper(0, len(s) - 1)
