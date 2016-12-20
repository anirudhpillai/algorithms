# Thanks to the amazing Stefan Pochmann
# the trick is to first find all letters which don't occur
# atleast k times in s
# then recursively check all substrings in s which don't
# contain these letters (this is achieved by splitting s at these letters)


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))

        return len(s)
