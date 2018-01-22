class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        start = 0

        if not s[0].isdigit():
            while start < len(s) and not s[start].isdigit():
                start += 1
            return s[0:start] + self.decodeString(s[start:])

        while start < len(s) and s[start] != "[":
            start += 1

        rep = int(s[0:start])

        count = 1
        end = start + 1

        while end < len(s):
            if s[end] == "[":
                count += 1
            if s[end] == "]":
                count -= 1

            if count == 0:
                break

            end += 1

        return (rep * self.decodeString(s[start+1:end])) + self.decodeString(s[end+1:])
