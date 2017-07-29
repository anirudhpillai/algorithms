class Solution(object):
    def change(self, amount, coins):
        """DFS Solution
        result = 0

        def dfs(curr):
            global result
                return
            elif sum(curr) < amount:
                for i in [k for k in coins if not curr or k >= curr[-1]]:
                    dfs(curr + [i])
            else:
                result += 1
                return

        dfs([])
        return result
        """
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for i in coins:
            for j in range(i, amount+1):
                dp[j] += dp[j-i]

        return dp[-1]
