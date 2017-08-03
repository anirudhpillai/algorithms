class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] != 1:
                    if row == 0 and col == 0:
                        dp[row][col] = 1
                    elif row == 0:
                        dp[row][col] = dp[row][col-1]
                    elif col == 0:
                        dp[row][col] = dp[row-1][col]
                    else:
                        dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[-1][-1]
