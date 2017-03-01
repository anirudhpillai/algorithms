# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_than = lt = ListNode(0)
        greater_than_equal = gte = ListNode(0)

        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                gte.next = head
                gte = gte.next
            head = head.next

        gte.next = None
        lt.next = greater_than_equal.next

        return less_than.next
