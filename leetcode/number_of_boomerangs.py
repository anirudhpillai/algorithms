class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x1,y1 in points:
            dp = dict()
            for x2,y2 in points:
                dis = (x1-x2)**2 + (y1-y2)**2
                if dis in dp:
                    dp[dis] += 1
                else:
                    dp[dis] = 1
            for k in dp.values():
                ans += k*(k-1)
        return ans
