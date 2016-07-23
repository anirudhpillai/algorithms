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


# from itertools import permutations
#
# def answer(t, n):
#
#     def rec(N, n, T, t, seq):
#         if n > N or t > T or n < 1:
#             return seq
#
#         if n == N:
#             if t == T:
#                 return seq
#             else:
#                 return rec(N, n, T, t+1, seq + ['S'])
#
#         if n == 1:
#             return rec(N, n+1, T, t+1, seq + ['R']) or rec(N, n, T, t+1, seq + ['S'])
#
#         return rec(N, n+1, T, t+1, seq + ['R']) or rec(N, n, T, t+1, seq + ['S']) or rec(N, n-1, T, t+1, seq + ['L'])
#
#     seq = rec(n, 1, t, 0, [])
#     return count_iterable(permutations(seq)) % 123454321
#
# def count_iterable(i):
#     dp = {}
#     for j in i:
#         if str(j) not in str(dp):
#             dp[str(j)] = 1
#     return len(dp) % 123454321


# def answer(t, n):
#
#     dp = {}
#
#     def rec(N, n, T, t, seq):
#         if n > N or t > T or n < 1:
#             return
#
#         if n == N:
#             if t == T:
#                 dp[str(seq)] = 1
#                 return
#             else:
#                 rec(N, n, T, t+1, seq + ['S'])
#                 return
#
#         if n == 1:
#             rec(N, n+1, T, t+1, seq + ['R'])
#             rec(N, n, T, t+1, seq + ['S'])
#             return
#
#         rec(N, n+1, T, t+1, seq + ['R'])
#         rec(N, n, T, t+1, seq + ['S'])
#         rec(N, n-1, T, t+1, seq + ['L'])
#
#         return
#
#     rec(n, 1, t, 0, [])
#     return len(dp) % 123454321
