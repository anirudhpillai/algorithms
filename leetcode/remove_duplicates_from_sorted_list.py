class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = forward = head

        while forward:
            while forward and p.val == forward.val:
                forward = forward.next
            p.next = forward
            p = p.next

        return head
