class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        p = head

        while p:
            if p.val == val:
                prev.next = p.next
            else:
                prev = p
            p = p.next

        return dummy.next
