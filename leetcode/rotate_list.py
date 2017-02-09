# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        l = 1
        end = head

        while end.next:
            end = end.next
            l += 1

        tail = head

        if ((l-k) % l)-1 < 0:
            return head

        for i in range(((l-k) % l)-1):
            tail = tail.next

        end.next = head
        start = tail.next
        tail.next = None

        return start
