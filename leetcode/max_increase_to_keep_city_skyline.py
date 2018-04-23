class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lr_skyline = [max(row) for row in grid]
        tb_skyline = []
        
        for col_idx in range(len(grid[0])):
            tb_skyline.append(max(row[col_idx] for row in grid))
        
        result = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                height = min(lr_skyline[r], tb_skyline[c])
                result += height - grid[r][c]
                    
        return result
