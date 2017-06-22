from math import factorial

C_dp = dict()
answer_helper_dp = dict()


def C(n, k):
    if (n, k) in C_dp:
        return C_dp[(n, k)]
    d = n - k
    if d < 0:
        return 0
    C_dp[(n, k)] = factorial(n) // factorial(k) // factorial(d)
    return C_dp[(n, k)]


def answer_helper(n, k):

    if (n, k) in answer_helper_dp:
        return answer_helper_dp[(n, k)]

    s = n * (n - 1) // 2

    if k == n - 1:
        ret = int(pow(n, (n - 2)))
    else:
        ret = C(s, k)
        for m in range(0, n - 1):
            temp = 0
            l = max(0, k - (m + 1) * m // 2)
            for p in range(l, k - m + 1):
                np = (n - 1 - m) * (n - 2 - m) // 2
                temp += C(np, p) * answer_helper(m + 1, k - p)

            ret -= C(n - 1, m) * temp

    answer_helper_dp[(n, k)] = ret

    return ret


def answer(N, K):
    return str(answer_helper(N, K))


print(answer(4, 3))
