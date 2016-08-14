# Given a binary search tree T, where each node contains a positive integer,
# and an integer K, you have to find whether or not there exist two different
# nodes A and B such that A.value + B.value = K.
# Return 1 to denote that two such nodes exist. Return 0, otherwise.

def t2Sum(root, k):

    # do inorder traversal
    stack = []
    arr = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            temp = stack.pop()
            arr.append(temp.val)
            root = temp.right

    # find poir from array
    l, r = 0, len(arr) - 1

    while l < r:
        curr = arr[l] + arr[r]
        if curr == k:
            return 1
        elif curr < k:
            l += 1
        else:
            r -= 1

    return 0
