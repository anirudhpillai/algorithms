class Solution(object):
    def checkValidString(self, s):
        max_count = min_count = 0

        for c in s:
            if c != ")":
                max_count += 1
            else:
                max_count -= 1

            if c == "(":
                min_count += 1
            else:
                min_count -= 1

            if max_count < 0:
                return False

            min_count = max(min_count, 0)

        return min_count == 0

        """
        memo = {}

        def helper(rcount, idx):
            if (rcount, idx) in memo:
                return memo[(rcount, idx)]

            if rcount < 0:
                return False

            if idx >= len(s):
                return rcount == 0

            if s[idx] == "(":
                memo[(rcount, idx)] = helper(rcount + 1, idx + 1)
            elif s[idx] == ")":
                if rcount > 0:
                    memo[(rcount, idx)] = helper(rcount - 1, idx + 1)
                else:
                    memo[(rcount, idx)] = False
            else:
                memo[(rcount, idx)] = (
                    helper(rcount + 1, idx + 1)
                    or helper(rcount - 1, idx + 1)
                    or helper(rcount, idx + 1)
                )

            return memo[(rcount, idx)]

        return helper(0, 0)
        """
