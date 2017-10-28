def minimumMoves(a, m):
    def moves(a, m):
        a = list(map(int, list(str(a))))
        m = list(map(int, list(str(m))))
        result = 0
        for i in range(len(a)):
            result += abs(a[i] - m[i])
        return result

    result = 0
    for i in range(len(a)):
        result += moves(a[i], m[i])

    return result
