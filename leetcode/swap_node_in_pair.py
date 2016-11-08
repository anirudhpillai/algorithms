class Solution(object):
    def swapPairs(self, head):

        # modifying the list
        # if not head:
        #     return head
        # dummy = head
        #
        # def swap(n1, n2):
        #     temp = n1.val
        #     n1.val = n2.val
        #     n2.val = temp
        #
        # while head and head.next:
        #     swap(head, head.next)
        #     head = head.next.next
        #
        # return dummy

        if not head or not head.next:
            return head

        ret = head.next
        node = head

        def rec(p):
            if not p or not p.next:
                return p

            temp = p.next.next
            ret = p.next
            p.next.next = p
            p.next = rec(temp)
            return ret

        rec(node)

        return ret
