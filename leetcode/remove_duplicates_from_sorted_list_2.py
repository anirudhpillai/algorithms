class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        curr_val = head.val
        if head.next and head.val == head.next.val:
            while head and head.val == curr_val:
                head = head.next
            head = self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)

        return head
