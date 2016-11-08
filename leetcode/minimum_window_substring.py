"""
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".
"""


class Solution(object):
    def minWindow(self, s, t):

        result = ""

        table = dict()
        for i in t:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1

        count = len(table)  # unique chars in t

        l, r = 0, -1

        while r < len(s):
            if count == 0:  # l-r contains t
                if not result or r-l+1 < len(result):
                    result = s[l:r+1]

                if s[l] in table:
                    table[s[l]] += 1

                    if table[s[l]] > 0:
                        count += 1

                l += 1

            else:
                r += 1  # move r and add new char

                if r == len(s):
                    break

                if s[r] in table:
                    table[s[r]] -= 1

                    if table[s[r]] == 0:
                        count -= 1

        return result
