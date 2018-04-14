class Solution:
    def canIWin(self, max_int, target):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if target > (max_int + 1) * max_int / 2:
            return False

        memo = {}

        def helper(used, curr_target):
            if used in memo:
                return memo[used]

            for i in range(1, max_int + 1):
                if not (used & (1 << i)):
                    used = used | (1 << i)

                    if curr_target - i <= 0 or not helper(used, curr_target - i):
                        used = used & (~(1 << i))
                        memo[used] = True
                        return True

                    used = used & (~(1 << i))


            memo[used] = False
            return False

        return helper(0, target)
    
