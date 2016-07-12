from itertools import permutations

def answer(t, n):

    def rec(N, n, T, t, seq):
        if n > N or t > T or n < 1:
            return seq

        if n == N:
            if t == T:
                return seq
            else:
                return rec(N, n, T, t+1, seq + ['S'])

        if n == 1:
            return rec(N, n+1, T, t+1, seq + ['R']) or rec(N, n, T, t+1, seq + ['S'])

        return rec(N, n+1, T, t+1, seq + ['R']) or rec(N, n, T, t+1, seq + ['S']) or rec(N, n-1, T, t+1, seq + ['L'])

    seq = rec(n, 1, t, 0, [])
    return count_iterable(permutations(seq)) % 123454321

def count_iterable(i):
    dp = {}
    for j in i:
        if str(j) not in str(dp):
            dp[str(j)] = 1
    return len(dp) % 123454321
