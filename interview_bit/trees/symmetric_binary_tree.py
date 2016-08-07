def isSymmetric(node):
        if not node:
            return 1
        return 1 if check(node.left, node.right) else 0

def check(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    if left.val != right.val:
        return False
    else:
        return check(left.left, right.right) and check(left.right, right.left)
