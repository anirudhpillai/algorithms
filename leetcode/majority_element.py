class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp = dict()
        # for i in nums:
        #     if i in dp:
        #         dp[i] += 1
        #     else:
        #         dp[i] = 1

        # for i, v in dp.iteritems():
        #     if v > len(nums)/2:
        #         return i

        # return -1

        result, count = 0, 0

        for i in nums:
            if count == 0:
                result = i
                count = 1
            elif i == result:
                count += 1
            else:
                count -= 1

        return result
        
