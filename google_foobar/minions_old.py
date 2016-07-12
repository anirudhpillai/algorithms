def answer(t, n):

    dp = {}

    def rec(N, n, T, t, seq):
        if n > N or t > T or n < 1:
            return

        if n == N:
            if t == T:
                dp[str(seq)] = 1
                return
            else:
                rec(N, n, T, t+1, seq + ['S'])
                return

        if n == 1:
            rec(N, n+1, T, t+1, seq + ['R'])
            rec(N, n, T, t+1, seq + ['S'])
            return

        rec(N, n+1, T, t+1, seq + ['R'])
        rec(N, n, T, t+1, seq + ['S'])
        rec(N, n-1, T, t+1, seq + ['L'])

        return

    rec(n, 1, t, 0, [])
    return len(dp) % 123454321
