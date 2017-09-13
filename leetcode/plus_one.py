class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 1

        for digit in reversed(digits):
            curr_digit = digit + carry

            if curr_digit > 9:
                curr_digit -= 10
                carry = 1
            else:
                carry = 0

            result.append(curr_digit)

        if carry:
            result.append(1)

        return list(reversed(result))
