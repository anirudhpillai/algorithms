class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        result = 0
        intervals.sort(key=lambda x: x.start)
        end = 0

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[end].end:
                result += 1
                if intervals[i].end < intervals[end].end:
                    end = i
            elif intervals[i].end > intervals[end].end:
                end = i

        return result
