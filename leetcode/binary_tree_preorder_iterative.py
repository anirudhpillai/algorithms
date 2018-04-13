def iterative_preorder(root):
    if not root:
        return

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            # add right first so that left gets processed first
            stack.append(node.right)
            stack.append(node.left)

    return result
