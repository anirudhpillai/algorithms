def unique_paths(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1

    dp = [[0 for i in range(n)] for i in range(m)]

    for i in range(m):
        dp[i][0] = 1

    for i in range(n):
        dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    for i in dp:
        print(i)

    return dp[m-1][n-1]

print(unique_paths(2, 2))
