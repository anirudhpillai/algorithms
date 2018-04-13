def iterative_postorder(root):
    if not root:
        return

    result = []
    stack = []

    while stack:
        node = s1.pop()
        if node:
            result.append(node.val)
            # left before as order reversed when added to s2
            # so right processed first
            stack.append(node.left)
            stack.append(node.right)

    return result[::-1]  # reverse
