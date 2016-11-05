def lcs(a, b):
    maximum = 0
    dp = [[0 for i in b] for i in a]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i-1][j-1]

                maximum = max(maximum, dp[i][j])

    return maximum

print(lcs("abc", "abcd"))
