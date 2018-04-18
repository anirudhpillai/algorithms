import collections


class Solution:
    def findPairs(self, nums, k):
        """
        num_to_freq = {}
        result = 0

        for num in nums:
            num_to_freq[num] = num_to_freq.get(num, 0) + 1

        for num in num_to_freq:
            if (
                (k == 0 and num_to_freq[num] > 1)
                or (k > 0 and num + k in num_to_freq)
            ):
                result += 1

        return result
        """

        freq = collections.Counter(nums)
        """
        result = 0

        for num in freq:
            if (
                (k == 0 and freq[num] > 1)
                or (k > 0 and num + k in freq)
            ):
                result += 1

        return result
        """

        return sum((k == 0 and freq[num] > 1) or (k > 0 and num + k in freq) for num in freq)
