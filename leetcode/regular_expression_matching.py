class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return s == ""

        # p[1] is not "*"
        if len(p) <= 1 or p[1] != "*":
            return (
                (s != "")
                and (p[0] == s[0] or p[0] == ".")
                and self.isMatch(s[1:], p[1:])
            )

        i = 0

        # while s[i] matches p[0]
        while i < len(s) and (p[0] == s[i] or p[0] == "."):
            if self.isMatch(s[i+1:], p[2:]):
                return True
            i += 1

        # * goes to 0 occurence
        return self.isMatch(s, p[2:])
