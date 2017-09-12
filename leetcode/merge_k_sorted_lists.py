# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        dummy = head
        queue = PriorityQueue()

        for node in lists:
            if node:
                queue.put((node.val, node))

        while not queue.empty():
            least_val, least = queue.get()
            dummy.next = ListNode(least_val)
            dummy = dummy.next
            least = least.next
            if least:
                queue.put((least.val, least))

        return head.next
