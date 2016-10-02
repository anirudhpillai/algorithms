"""
Divide two integers without using multiplication,
division and mod operator.

If it is overflow, return MAX_INT.
"""


import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            return (2 ** 31) - 1
        if divisor == -1 and dividend == -(2 ** 31):
            return (2 ** 31) - 1

        pDividend = abs(dividend)
        pDivisor = abs(divisor)

        result = 0

        while pDividend >= pDivisor:
            shifts = 0

            while pDividend >= (pDivisor << shifts):
                shifts += 1

            result += 1 << (shifts -1)
            pDividend -= (pDivisor << (shifts - 1))

        if (divisor < 0) ^ (dividend < 0):
            return -result
        else:
            return result
