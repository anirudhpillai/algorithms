class Solution:
    def preimageSizeFZF(self, K):
        """
        Beats 95.28%
        """
        def trailing_zeroes(num):
            result = 0

            while num:
                num = num // 5
                result += num

            return result

        l, r = 0, 5 * (K + 1)

        while l <= r:
            mid = (l + r) // 2
            zeroes = trailing_zeroes(mid)

            if zeroes < K:
                l = mid + 1
            elif zeroes > K:
                r = mid - 1
            else:
                # answer is always either 5 or 0
                return 5

        return 0
