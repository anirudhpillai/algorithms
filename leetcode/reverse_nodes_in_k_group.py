"""
Given a linked list, reverse the nodes of a
linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then
left-out nodes in the end should remain as it is.

You may not alter the values in the nodes,
only nodes itself may be changed.

Only constant memory is allowed.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        if not head:
            return None

        l = 0
        p = head
        while p:
            p = p.next
            l += 1
            if l >= k:
                break

        if l < k:
            return head

        prev = None
        p = head

        for i in range(k):
            temp = p.next
            p.next = prev
            prev = p
            p = temp

        ret = prev
        head.next = self.reverseKGroup(p, k)

        return ret
