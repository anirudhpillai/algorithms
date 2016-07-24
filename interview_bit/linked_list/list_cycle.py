# Solution with constant space
# First meeting point will be inside the cycle
# then reset slow to head and move both at same pace
# they are guaranteed to meet at the start of the cycle
# explanation is here http://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work

def detectCycle(self, A):
        slow, fast = A, A
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = A
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None



# Solution with Hashing
# def detectCycle(A):
#         seen = set()
#         while A:
#             if A.val in seen:
#                 return A
#             else:
#                 seen.add(A.val)
#                 A = A.next
