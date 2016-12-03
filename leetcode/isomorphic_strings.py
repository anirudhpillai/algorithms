"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s
can be replaced to get t.

All occurrences of a character must be replaced with
another character while preserving the order of characters.
No two characters may map to the same character but a
character may map to itself.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        table = dict()

        for i in range(len(s)):
            if s[i] not in table:
                if t[i] in table.values():
                    return False
                table[s[i]] = t[i]

            elif table[s[i]] != t[i]:
                return False

        return True


# One line magic by AntaresTsao
class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
