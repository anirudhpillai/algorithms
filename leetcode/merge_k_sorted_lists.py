"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""


from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Solution using PriorityQueue
Complexity: nlog(k)
where n is total number of elements and k is number of lists
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return None

        queue = PriorityQueue()

        for list in lists:
            if list:
                queue.put((list.val, list))

        head = ListNode(0)
        p = head

        while not queue.empty():
            n = queue.get()[1]
            p.next = n
            p = p.next

            if n.next:
                queue.put((n.next.val, n.next))

        return head.next
