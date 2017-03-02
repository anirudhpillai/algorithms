class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if num_rows == 1:
            return s

        rows = ["" for _ in range(num_rows)]

        curr_row, direction = 0, 1

        for i in s:
            rows[curr_row] += i

            if curr_row == 0:
                direction = 1
            elif curr_row == num_rows-1:
                direction = -1

            curr_row += direction

        return "".join(rows)
