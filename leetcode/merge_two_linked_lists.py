# interative solution
def merge_two_linked_lists(l1, l2):
    ret = ListNode(0)
    head = ret

    i, j = l1, l2

    if not l1 and not l2:
        return None

    if not l1:
        return l2

    if not l2:
        return l1

    while i and j:
        if i.val < j.val:
            head.next = ListNode(i.val)
            head = head.next
            i = i.next
        else:
            head.next = ListNode(j.val)
            head = head.next
            j = j.next

    while i:
        head.next = ListNode(i.val)
        head = head.next
        i = i.next

    while j:
        head.next = ListNode(j.val)
        head = head.next
        j = j.next

    return ret.next


# recursive solution
def merge_two_linked_lists(l1, l2):
    if not l1:
            return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = merge_two_linked_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_linked_lists(l2.next, l1)
        return l2
