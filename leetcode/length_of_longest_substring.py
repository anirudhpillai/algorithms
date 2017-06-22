class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start_index = 0
        maximum = 0
        index_map = {}

        for current_index in range(len(s)):
            letter = s[current_index]

            if letter in index_map:
                start_index = max(index_map[letter] + 1, start_index)

            index_map[letter] = current_index
            maximum = max(maximum, current_index - start_index + 1)

        return maximum


# Less Efficient
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         start_index = 0
#         maximum = 0
#         i = 0
#         last_seen = {}
#
#         for i, letter in enumerate(s):
#             if letter in last_seen:
#                 new_start = last_seen[letter] + 1
#
#                 for j in range(start_index, new_start):
#                     last_seen.pop(s[j])
#
#                 maximum = max(maximum, i - start_index)
#                 start_index = new_start
#
#             last_seen[letter] = i
#
#         return max(maximum, len(s) - start_index)
