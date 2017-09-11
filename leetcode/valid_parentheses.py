class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            elif stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False

        return True if not stack else False
