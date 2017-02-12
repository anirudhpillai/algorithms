# def max_envelopes(envelopes):
#     """
#     O(n^2) solution
#     """
#     envelopes.sort(key=lambda x: x[0])
#     dp = [1 for _ in envelopes]
#
#     print(envelopes)
#
#     for i in range(len(envelopes)):
#         for j in range(i+1, len(envelopes)):
#             if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
#                 dp[j] = max(dp[i] + 1, dp[j])
#
#     return max(dp) if envelopes else 0

from functools import cmp_to_key


def max_envelopes(envelopes):
    """
    O(nlogn) solution, inspired from @agave
    :type envelopes: List[List[int]]
    :rtype: int
    """
    def compare(a, b):
        if a[0] == b[0]:
            return b[1] - a[1]
        else:
            return a[0] - b[0]

    envelopes.sort(key=cmp_to_key(compare))

    def lmip(tails, k):
        l, h = 0, len(tails) - 1
        while l <= h:
            m = (l + h) // 2
            if envelopes[tails[m]][1] >= k[1]:
                h = m - 1
            else:
                l = m + 1
        return l

    tails = []
    for i, env in enumerate(envelopes):
        idx = lmip(tails, env)
        if idx >= len(tails):
            tails.append(i)
        else:
            tails[idx] = i

    return len(tails)


print(max_envelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 9], [1, 3]]))
