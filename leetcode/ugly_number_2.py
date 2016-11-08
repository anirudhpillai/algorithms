class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        result = [1]

        i, j, k = 0, 0, 0

        while len(result) < n:
            m2 = result[i] * 2
            m3 = result[j] * 3
            m5 = result[k] * 5

            minimum = min(m2, m3, m5)
            result.append(minimum)

            if minimum == m2:
                i += 1

            if minimum == m3:
                j += 1

            if minimum == m5:
                k += 1

        return result[-1]


def is_ugly(num):
    if num == 0:
        return False
    if num == 1:
        return True

    if num % 2 == 0:
        num = num/2
        return is_ugly(num)

    if num % 3 == 0:
        num = num/3
        return is_ugly(num)

    if num % 5 == 0:
        num = num/5
        return is_ugly(num)

    return False
