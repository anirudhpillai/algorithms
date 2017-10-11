class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def swap(node):
            if not node or not node.next:
                return node

            new_head = node.next
            leftover_list = node.next.next
            node.next.next = node
            node.next = swap(leftover_list)
            return new_head

        return swap(head)
