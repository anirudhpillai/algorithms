"""
Given N * M field of O's and X's, where O=white, X=black
Return the number of black shapes. A black shape consists
of one or more adjacent X's (diagonals not included)
"""


def black(A):
    A = map(list, A)

    def nullify(x, y):
        if 0 <= x < len(A) and 0 <= y < len(A[0]):
            if A[x][y] == 'X':
                A[x][y] = 'O'
                nullify(x+1, y)
                nullify(x-1, y)
                nullify(x, y+1)
                nullify(x, y-1)
                return

    ans = 0

    for x in range(len(A)):
        for y in range(len(A[0])):
            if A[x][y] == 'X':
                ans += 1
                nullify(x, y)

    return ans
