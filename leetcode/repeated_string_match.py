class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        mult = len(B) // len(A)
        
        if B in A * mult:
            return mult
        
        if B in A * (mult + 1):
            return mult + 1
        
        if B in A * (mult + 2):
            return mult + 2
        
        return -1
