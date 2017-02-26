class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        prev, slow, fast = None, head, head

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if prev:
            prev.next = None
        else:
            head = None

        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node
