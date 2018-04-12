class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        if n == 0:
            return 1

        if n == 1:
            return 10

        def helper(curr_n, multiple):
            if not curr_n:
                return 1

            return multiple * helper(curr_n - 1, multiple - 1)

        return 9 * helper(n-1, 9) + self.countNumbersWithUniqueDigits(n-1)
        """

        # The runtime for the one below beats 100%
        result, product = 1, 1
        dp = [9] + list(reversed(range(1, 10)))

        for i in range(n if n < 10 else 10):
            product *= dp[i]
            result += product

        return result
