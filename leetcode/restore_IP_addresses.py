class Solution:
    def restoreIpAddresses(self, s):
        """
        Beats 95%
        """

        def helper(curr, dots_left):
            if not curr or len(curr) > 3 * (dots_left + 1):
                return []

            if dots_left == 0 and int(curr) < 256 and (
                len(curr) == 1 or curr[0] != "0"
            ):
                return [curr]

            result = []

            if curr[0] == "0":
                for rest in helper(curr[1:], dots_left - 1):
                    result.append(curr[0] + "." + rest)
                return result

            for i in range(3):
                if int(curr[:i+1]) < 256:
                    for rest in helper(curr[i+1:], dots_left - 1):
                        result.append(curr[:i+1] + "." + rest)

            return result

        return helper(s, 3)
