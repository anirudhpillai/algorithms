class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        dp = [0 for i in range(len(A))]
        A = map(int, list(A))

        if A[0] > 0:
            dp[0] = 1

        for i in range(1, len(A)):
            if A[i] > 0:
                dp[i] += dp[i-1]

            if A[i-1]*10 + A[i] <= 26 and A[i-1]*10 + A[i] >= 10:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]

        return dp[len(A)-1]
