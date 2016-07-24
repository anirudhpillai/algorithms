def lPalin(A):

        l = 0
        head = A
        while head:
            l += 1
            head = head.next

        rev = A

        for i in range(l/2):
            rev = rev.next

        prev = None

        while rev.next:
            temp = rev.next
            rev.next, prev, rev = prev, rev, temp
        rev.next = prev

        head = A
        while rev:
            if rev.val != head.val:
                return 0
            head = head.next
            rev = rev.next

        return 1

# So, use is when and only when you are comparing object identities. Use == when comparing values.
# is checks for object identity equivalence
# This would have saved me a lot of time
