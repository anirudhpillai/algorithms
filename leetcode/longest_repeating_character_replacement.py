class Solution(object):
    def characterReplacement(self, s, k):
        """
        Classic Sliding Window
        """

        count = {}
        m = start = result = 0

        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            m = max(m, count[s[end]])

            # end - start + 1 is the len of the substring
            # if no of letters != m (the rep letter) > k the move window
            if end - start + 1 - m > k:
                count[s[start]] -= 1
                start += 1

            result = max(result, end - start + 1)

        return result
