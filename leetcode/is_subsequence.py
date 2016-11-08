class Solution(object):
    def isSubsequence(self, S, T):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not S:
            return True
        if not T:
            return False

        s = 0

        for t in T:
            if t == S[s]:
                s += 1
                if s >= len(S):
                    return True

        return False
