class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for d in num:
            while stack and stack[-1] > d and k > 0:  # char so can compare
                stack.pop()
                k -= 1
            stack.append(d)

        return "".join(stack[:-k or None]).lstrip("0") or "0"

        # First brute force attempt
        # if k == 0:
        #     return num

        # if len(num) == k:
        #     return "0"

        # mi = int(num)
        # for i in range(len(num)):
        #     mi = min(mi, int(num[:i] + num[i+1:]))

        # return self.removeKdigits(str(mi), k-1)
