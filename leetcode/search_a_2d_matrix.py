class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            curr = matrix[mid // cols][mid % cols]
            
            if curr == target:
                return True
            elif curr < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return False
        
