class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []

        def dfs(indices, curr_idx, path):
            if curr_idx == n:
                result.append(list(path))
                return

            for i in range(n):
                indices[curr_idx] = i
                if is_valid(indices, curr_idx):
                    row = "." * i + "Q" + "." * (n - (i + 1))
                    path.append(row)
                    dfs(indices, curr_idx + 1, path)
                    path.pop()

        def is_valid(indices, curr_idx):
            for i in range(curr_idx):
                if (
                    indices[i] == indices[curr_idx]
                    or abs(indices[i] - indices[curr_idx]) == curr_idx - i
                ):
                    return False

            return True

        dfs([-1] * n, 0, [])
        return result
