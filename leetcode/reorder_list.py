class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        index_to_node = {}
        p = head
        i = 0

        while p:
            index_to_node[i] = p
            p = p.next
            i += 1

        prev = None
        for j in range(i // 2 + 1):
            if prev:
                prev.next = index_to_node[j]

            if j == i // 2:
                index_to_node[j].next = None
                break

            index_to_node[j].next = index_to_node[i-j-1]
            prev = index_to_node[i-j-1]
