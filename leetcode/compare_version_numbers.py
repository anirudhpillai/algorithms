class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split("."), version2.split(".")
        swapped = 1

        if len(v2) < len(v1):
            swapped = -1
            v1, v2 = v2, v1

        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1 * swapped
            elif int(v1[i]) < int(v2[i]):
                return -1 * swapped

        for i in range(len(v1), len(v2)):
            if int(v2[i]) > 0:
                return -1 * swapped

        return 0
