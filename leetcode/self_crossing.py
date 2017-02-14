class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        Only thing to remember is apart from these cases if you think about any
        other case. Then for that case to be successful, one of these cases
        will also have to be successful.
        """
        for i in range(3, len(x)):
            # curr line crosses line curr+3
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            # curr line crosses line curr+4
            elif i >= 4 and x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                return True
            # curr line crosses line curr+6
            elif i >= 5 and x[i-2] >= x[i-4] and x[i-4] + x[i] >= x[i-2] \
                    and x[i-1] <= x[i-3] and x[i-3] <= x[i-5] + x[i-1]:
                return True

        return False
