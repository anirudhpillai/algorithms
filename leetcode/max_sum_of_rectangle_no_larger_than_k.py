class Solution:
    def maxSumSubmatrix(self, matrix, target):
        """
        O(n^4)
        """
        rows, cols = len(matrix), len(matrix[0])

        memo = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                memo[r][c] += matrix[r][c]
                if r == 0:
                    memo[r][c] += memo[r][c-1]
                elif c == 0:
                    memo[r][c] += memo[r-1][c]
                else:
                    memo[r][c] += memo[r-1][c] + memo[r][c-1] - memo[r-1][c-1]

        result = -1e9

        for r1 in range(rows):
            for c1 in range(cols):
                for r2 in range(r1, rows):
                    for c2 in range(c1, cols):
                        sum_of_rect = memo[r2][c2]
                        if r1 > 0:
                            sum_of_rect -= memo[r1-1][c2]
                        if c1 > 0:
                            sum_of_rect -= memo[r2][c1-1]
                        if r1 > 0 and c1 > 0:
                            sum_of_rect += memo[r1-1][c1-1]

                        if sum_of_rect <= target:
                            result = max(result, sum_of_rect)

        return result
