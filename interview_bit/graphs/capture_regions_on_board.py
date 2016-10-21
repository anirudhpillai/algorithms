"""
Given a 2D board containing 'X' and 'O',
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's
into 'X's in that surrounded region.
"""


def solve(self, A):

    def change(x, y):
        if 0 <= x < len(A) and 0 <= y < len(A[0]):
            if A[x][y] == 'O':
                A[x][y] = 'B'
                change(x+1, y)
                change(x-1, y)
                change(x, y+1)
                change(x, y-1)

    # left and right boundary
    for x in range(len(A)):
        if A[x][0] == 'O':
            change(x, 0)
        if A[x][len(A[0])-1] == 'O':
            change(x, len(A[0])-1)

    # top and bottom boundary
    for y in range(len(A[0])):
        if A[0][y] == 'O':
            change(0, y)
        if A[len(A)-1][y] == 'O':
            change(len(A)-1, y)

    for x in range(len(A)):
        for y in range(len(A[0])):
            if A[x][y] == 'O':
                A[x][y] = 'X'
            elif A[x][y] == 'B':
                A[x][y] = 'O'

    return A
