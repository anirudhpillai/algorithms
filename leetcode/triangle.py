class Solution:
    def minimumTotal(self, triangle):
        """ Top down dp O(n^2) space, I think
        memo = {}

        def helper(row, col):
            if row >= len(triangle):
                return 0

            if not (0 <= col < len(triangle[row])):
                return 1e9

            if (row, col) in memo:
                return triangle[row][col] + memo[(row, col)]

            memo[(row, col)] = min(
                helper(row + 1, col),
                helper(row + 1, col + 1)
            )

            return triangle[row][col] + memo[(row, col)]

        return helper(0, 0)
        """
        # Beats 97.45%
        # Bottoms up O(n) space where n is no of rows
        # Logic: adjacent nums share a branch
        dp = [0] * (len(triangle[-1]))

        for row in reversed(triangle[1:]):
            for i in range(len(dp)):
                dp[i] += row[i]

            next_dp = []
            for i in range(len(row)-1):
                next_dp.append(min(dp[i], dp[i+1]))

            dp = next_dp

        return dp[0] + triangle[0][0]
