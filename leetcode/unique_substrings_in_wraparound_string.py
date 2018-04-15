class Solution:
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        result = set()

        def next_to(l1, l2):
            l1, l2 = ord(l1) - ord("a"), ord(l2) - ord("a")
            return (l1 + 1) % 26 == l2

        counts = {}
        i = 0

        while i < len(p):
            end = i + 1

            for j in range(i + 1, len(p)):
                if not next_to(p[j-1], p[j]):
                    break
                end += 1

            counts[p[i]] = max(
                counts.get(p[i], 0),
                end - i
            )

            for j in range(i + 1, end):
                counts[p[j]] = max(
                    counts.get(p[j], 0),
                    counts[p[j-1]] - 1
                )

            i = end

        return sum(counts.values())
