import heapq


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heapq.heappush(self.intervals, (val, [val, val]))
        
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        
        while self.intervals:
            _, heap_top = heapq.heappop(self.intervals)
            if stack:
                _, stack_top = stack[-1]
                if stack_top[1] + 1 >= heap_top[0]:
                    stack[-1] = (stack_top[0], [stack_top[0], max(stack_top[1], heap_top[1])])
                else:
                    stack.append((heap_top[0], heap_top))
            else:
                stack.append((heap_top[0], heap_top))
                
        self.intervals = stack
        return list(map(lambda x: x[1], self.intervals))
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
