def answer(t, n):
    dp = {}
    def rec(t, p):
        if (t, p) in dp:
            return dp[(t, p)]
        elif p < 1 or t < n-p:
            return 0
        elif p is n or t == n-p:
            return 1
        else:
            u = t-1
            res = (rec(u, p-1) + rec(u, p) + rec(u, p+1)) % 123454321
            dp[(t, p)] = res
            return res
    return rec(t, 1)

print(answer(3, 2))
