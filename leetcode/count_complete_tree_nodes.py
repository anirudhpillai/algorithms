def count_nodes(root):

    if not root:
        return 0

    def height_left(node, curr):
        if not node:
            return curr

        return height_left(node.left, curr+1)

    def height_right(node, curr):
        if not node:
            return curr

        return height_right(node.right, curr+1)

    left = height_left(root, 0)
    right = height_right(root, 0)

    print(left, right)

    if left == right:
        return (2**left)-1
    else:
        return count_nodes(root.left)+count_nodes(root.right)+1
