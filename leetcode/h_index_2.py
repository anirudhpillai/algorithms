class Solution:
    def hIndex(self, citations):
        l, r = 0, len(citations) - 1
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if citations[mid] >= len(citations) - mid:
                result = len(citations) - mid
                r = mid - 1
            else:
                l = mid + 1

        return result
