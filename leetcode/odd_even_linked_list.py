class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even_dummy = ListNode(0)
        odd_dummy = ListNode(0)

        pe = even_dummy
        po = odd_dummy
        p = head
        odd = True

        while p:
            if odd:
                po.next = p
                po = po.next
                odd = False
            else:
                pe.next = p
                pe = pe.next
                odd = True
            p = p.next

        pe.next = None
        po.next = even_dummy.next
        return odd_dummy.next
