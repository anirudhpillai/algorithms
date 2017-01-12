def numSquares(n):
    """DP solution"""
    dp = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        m = 10000
        for j in range(1, int(i**0.5)+1):
            m = min(m, dp[i - j*j] + 1)
        dp[i] = m
    print(dp)
    return dp[n]

    """BFS solution
    s = [i*i for i in range(1,int(math.sqrt(n))+1)] # Square numbers <= n
    l = 0  # BFS level
    currentLevel = [0]  # List of numbers in BFS level l

    while True:
        nextLevel = []
        for a in currentLevel:
        for b in s:
            if a+b == n: return l+1  # Found n
            if a+b < n:  nextLevel.append(a+b)
        currentLevel = list(set(nextLevel))  # Remove duplicates
        l += 1
    """


print(numSquares(13))
