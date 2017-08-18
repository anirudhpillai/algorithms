class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1, m2, m3, s1, s2 = -1e9, -1e9, -1e9, 1e9, 1e9
        
        for i in nums:
            if i > m1:
                m1, m2, m3 = i, m1, m2
            elif i > m2:
                m2, m3 = i, m2
            elif i > m3:
                m3 = i
                
            if i < s1:
                s1, s2 = i, s1
            elif i < s2:
                s2 = i
                
        return max(m1*m2*m3, s1*s2*m1)
        
