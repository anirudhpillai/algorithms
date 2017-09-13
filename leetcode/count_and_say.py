class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def say(curr):
            if not curr:
                return ""

            count = 1
            while count < len(curr) and curr[count] == curr[count - 1]:
                count += 1

            return str(count) + str(curr[0]) + say(curr[count:])

        curr = "1"
        for _ in range(n-1):
            curr = say(curr)

        return curr
