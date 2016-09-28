def addTwoNumbers(A, B):
        carry = 0
        ret = ListNode(0)
        head = ret
        while A or B:
            if A:
                carry += A.val
                A = A.next
            if B:
                carry += B.val
                B = B.next

            head.next = ListNode(carry % 10)
            head = head.next

            carry = 1 if carry > 9 else 0

        if carry > 0:
            head.next = ListNode(carry)

        return ret.next
