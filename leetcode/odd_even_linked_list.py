# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = head.next
        podd, peven = odd, even
        while peven:
            if not peven.next:
                break
            podd.next = peven.next
            peven.next = peven.next.next

            podd = podd.next
            peven = peven.next

        podd.next = even
        return odd
