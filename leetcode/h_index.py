class Solution(object):
    def hIndex(self, citations):
        buckets = [0] * (len(citations)+1)

        for c in citations:
            if c > len(citations):
                buckets[len(citations)] += 1
            else:
                buckets[c] += 1

        total = 0

        for i in reversed(range(len(buckets))):
            total += buckets[i]
            if total >= i:
                return i

        return 0

        """Without Bucket Sort
        citations.sort(reverse=True)

        i = 0

        while i < len(citations):
            if i >= citations[i]:
                return i
            i += 1

        return i
        """
