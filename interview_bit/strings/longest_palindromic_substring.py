# expanding from center of palindrome
# 2n - 1 centers as center can be between letters
def lps(s):
    if not s or len(s) == 1:
        return s

    def helper(begin, end):
        while begin >= 0 and end <= len(s)-1 and s[begin] == s[end]:
            begin -= 1
            end += 1
        return s[begin+1:end]

    longest = s[0:1]
    for i in range(len(s)):
        # get longest palindrome with center at i
        temp = helper(i, i)
        if len(temp) > len(longest):
            longest = temp

        # get longest palindrome with center at i, i+1 (between letter)
        temp = helper(i, i+1)
        if len(temp) > len(longest):
            longest = temp

    return longest

# using dp in O(n^2) memory
# def lps(A):
#     if not A or len(A) <= 1:
#         return A
#
#     max_len = 0
#     dp = [[False for i in A] for i in A]
#
#     longest = None
#     # l is length, i is index of left boundary, j is index of right boundary
#     for l in range(len(A)):
#         for i in range(0, len(A)-l):
#             j = i+l
#             if A[i] == A[j] and (j-i < 2 or dp[i+1][j-1] == True):
#                 dp[i][j] = True
#
#                 if j-i+1 > max_len:
#                     max_len = j-i+1
#                     longest = A[i:j+1]
#     return longest

print(lps("aaaabaaa"))
