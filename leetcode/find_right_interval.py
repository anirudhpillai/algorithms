# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        sorted_start = sorted((interval.start, i) for i, interval in enumerate(intervals))
        sorted_end = sorted((interval.end, i) for i, interval in enumerate(intervals))
        
        result = [-1] * len(intervals)
        i = 0
        
        for start in sorted_start:
            while start[0] >= sorted_end[i][0]:
                result[sorted_end[i][1]] = start[1]
                i += 1
        
        return result
        
        """
        result = []
        comp = sorted(zip(range(len(intervals)), intervals), key=lambda x: x[1].start)
        print(comp)
        
        for i in range(len(intervals)):
            curr_min = -1
            for j in range(len(intervals)):
                if j != i and intervals[j].start >= intervals[i].end:
                    if curr_min == -1 or intervals[j].start < intervals[curr_min].start:
                        curr_min = j
            result.append(curr_min)
            
        return result
        """
