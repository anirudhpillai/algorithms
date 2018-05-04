import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        Going from top left to bottom right but also efficiently
        minimising the size of the heap.
        """
        
        if not nums1 or not nums2:
            return []
        
        heap = [(nums1[0] + nums2[0], 0, 0)]
        result = []
        
        while heap and len(result) < k:
            _, x, y = heapq.heappop(heap)
            result.append([nums1[x], nums2[y]])
            
            if y == 0 and x + 1 < len(nums1):
                heapq.heappush(heap, (nums1[x + 1] + nums2[y], x + 1, y))
            
            if y + 1 < len(nums2):
                heapq.heappush(heap, (nums1[x] + nums2[y + 1], x, y + 1))
        
        return result


"""
def kSmallestPairs(self, nums1, nums2, k):
    streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
    stream = heapq.merge(*streams)
    return [suv[1:] for suv in itertools.islice(stream, k)]

def kSmallestPairs(self, nums1, nums2, k):
    queue = []
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0)
    pairs = []
    while queue and len(pairs) < k:
        _, i, j = heapq.heappop(queue)
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    return pairs
"""
