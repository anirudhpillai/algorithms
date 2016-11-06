class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        dp = {
            1: "1",
            2:  "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            0: "0"
        }

        result = []

        def rec(s, curr):
            if not s:
                result.append(curr)
                return

            for i in dp[int(s[0])]:
                rec(s[1:], curr+i)

        rec(A, "")
        return result
