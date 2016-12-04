class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer

    def wordBreak(self, A, B):

        # dp = [True] + [False]*len(A)

        # for i in range(len(A)):

        #     if not dp[i]:
        #         continue

        #     for word in B:
        #         if i+len(word) > len(A):
        #             continue
        #         if dp[i+len(word)]:
        #             continue

        #         if A[i:i+len(word)] == word:
        #             dp[i+len(word)] = True

        # return dp[len(A)]

        stack = [1]

        for i in range (0, len(A)):
            stack.append(0)
            for j in range(i,-1,-1):
                if stack[j] and A[j:i+1] in B:
                    stack[i+1] = 1
                    break

        return stack[len(A)]

        # if not A:
        #     return True

        # if A in self.dp:
        #     return self.dp[A]

        # for i in range(len(A)):
        #     if A[0:i+1] in B:
        #         if self.wordBreak(A[i+1:], B):
        #             self.dp[A] = True
        #             return True

        # self.dp[A] = False
        # return False
