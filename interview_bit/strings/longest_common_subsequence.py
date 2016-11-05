def lcs(a, b):
    dp = [[0 for i in range(len(b)+1)] for i in range(len(a)+1)]

    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    index = dp[len(a)][len(b)]

    lcs = ["" for i in range(index+1)]
    lcs[index] = '\0'

    i, j = len(a), len(b)

    while i > 0 and j > 0:
        # if char same in both then part of lcs
        if a[i-1] == b[j-1]:
            lcs[index-1] = a[i-1]
            i -= 1
            j -= 1
            index -= 1
        # else move in direction of greater cell
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)


print(lcs("ABCDGH", "AEDFHR"))
