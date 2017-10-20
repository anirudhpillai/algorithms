class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for s in strs:
            key = str(sorted(s))
            groups[key] = groups.get(key, []) + [s]

        return groups.values()
