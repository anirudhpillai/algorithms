class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        dp = [[-1 for i in range(len(B))] for i in range(len(A))]

        def solve(a, b):

            if a == len(A):
                return len(B) - b
            if b == len(B):
                return len(A) - a

            if dp[a][b] != -1:
                return dp[a][b]

            if A[a] == B[b]:
                dp[a][b] = solve(a+1, b+1)
            else:
                dp[a][b] = 1 + min(solve(a+1, b),
                                   solve(a, b+1),
                                   solve(a+1, b+1))

            return dp[a][b]

        return solve(0, 0)
