# thanks to StefanPochmann for this amazing pythonic code
# and sublime dictionary technique to do bfs


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(s):
            brackets = 0
            for i in s:
                if i == '(':
                    brackets += 1
                elif i == ')':
                    brackets -= 1
                    if brackets < 0:
                        return False
            return brackets == 0

        level = {s}

        while True:
            valid = filter(is_valid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
