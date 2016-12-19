# the trick is to start dp from bottom right not top left


def calculateMinimumHP(A):
    rows = len(A)
    cols = len(A[0])

    # dp has extra row and col
    dp = [[10000000 for _ in range(cols+1)] for _ in range(rows+1)]

    # we need to have atleast 1 when we reach the end
    dp[rows-1][cols] = 1
    dp[rows][cols-1] = 1

    for i in range(rows-1, -1, -1):
        for j in range(cols-1, -1, -1):
            need = min(dp[i][j+1], dp[i+1][j]) - A[i][j]
            # if we are gaining health on the path forward
            # we need just 1 at the current point
            # else we need whatever we will be losing
            dp[i][j] = 1 if need <= 0 else need

    return dp[0][0]
