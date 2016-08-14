# recursive
def inorder_recursive(root):
    values = []

    def traverse(root):
        if not root.left and not root.right:
            values.append(root.val)
            return
        if root.left:
            traverse(root.left)
        values.append(root.val)
        if root.right:
            traverse(root.right)

    traverse(root)
    return values

# iterative
def inorder_iterative(root):
    ret = []
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            node = stack.pop()
            ret.append(node.val)
            curr = node.right
    return ret
