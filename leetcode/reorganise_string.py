from queue import PriorityQueue


class Solution:
    def reorganizeString(self, S):
        """
        Similar to Task Scheduler
        """
        letter_map = {}
        queue = PriorityQueue()

        for c in S:
            letter_map[c] = letter_map.get(c, 0) + 1

        for k, v in letter_map.items():
            queue.put((-v, k))

        result = ""

        while not queue.empty():
            f1, l1 = queue.get()
            freq, letter = f1, l1

            if result and result[-1] == letter:
                if queue.empty():
                    return ""
                else:
                    f2, l2 = queue.get()
                    queue.put((f1, l1))
                    freq, letter = f2, l2

            result += letter
            freq = abs(freq) - 1
            if freq > 0:
                queue.put((-freq, letter))

        return result


"""
Also check out Rearrage string k distance apart.
Compare time complexity.

https://www.programcreek.com/2014/08/leetcode-rearrange-string-k-distance-apart-java/
"""
