class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                one, two = s[l+1:r+1], s[l:r]
                return one == one[::-1] or two == two[::-1]
            l += 1
            r -= 1

        return True
