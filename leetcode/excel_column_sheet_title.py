class Solution:
    def convertToTitle(self, n):
        """
        Beats 96.68%
        """
        if n == 0:
            return ""

        if n < 27:
            return chr(ord("a") + n - 1).upper()

        if n % 26:
            return self.convertToTitle(n // 26) + self.convertToTitle(n % 26)
        else:
            return self.convertToTitle((n // 26) - 1) + "Z"
