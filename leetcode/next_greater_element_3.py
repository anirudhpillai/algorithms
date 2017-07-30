class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))

        for i in reversed(range(len(n))):
            if i != 0 and int(n[i]) > int(n[i-1]):
                for j in reversed(range(len(n))):
                    if int(n[j]) > int(n[i-1]):
                        n[i-1], n[j] = n[j], n[i-1]
                        result = int("".join(n[:i] + (n[i:])[::-1]))
                        if result > (2**31 - 1):
                            return -1
                        else:
                            return result

        return -1
