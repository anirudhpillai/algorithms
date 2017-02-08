class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dp = [0] * 26

        for letter in magazine:
            dp[ord(letter) - ord('a')] += 1

        for letter in ransomNote:
            if dp[ord(letter) - ord('a')] == 0:
                return False
            else:
                dp[ord(letter) - ord('a')] -= 1

        return True
