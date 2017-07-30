class NumMatrix(object):

    def __init__(self, matrix):
        """
        The idea is simple, just precompute sums for all matrices with (0, 0)
        as top left corner and (i, j) as bottom right corner. There are O(n^2)
        of these matrices, so we store them in a 2D table. In order to make
        code simpler, I add an extra column and row, filled with 0.
        """
        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])

        self.dp = [[0]*(cols+1) for _ in range(rows+1)]

        for row in range(1, rows+1):
            for col in range(1, cols+1):
                self.dp[row][col] = (
                    matrix[row-1][col-1]  # as matrix size is < dp
                    + self.dp[row-1][col]
                    + self.dp[row][col-1]
                    - self.dp[row-1][col-1]
                )

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return (
            self.dp[row2+1][col2+1]
            - self.dp[row2+1][col1]
            - self.dp[row1][col2+1]
            + self.dp[row1][col1]
        )
