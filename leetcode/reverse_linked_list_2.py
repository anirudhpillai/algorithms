class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = p = ListNode(0)
        dummy.next = head

        for _ in range(m-1):
            p = p.next

        curr = p.next
        prev = None

        for i in range(n-m+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        p.next.next = curr
        p.next = prev

        return dummy.next
