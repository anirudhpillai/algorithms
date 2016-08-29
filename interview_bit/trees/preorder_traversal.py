def preorder_recursive(root):
    values = []
    def traverse(root):
        if not root:
            return
        values.append(root.val)
        traverse(root.left)
        traverse(root.right)
    traverse(root)
    return values

def preorder_iterative(root):
    ret = []
    stack = []
    while stack or root:
        if not root:
            root = stack.pop()
        else:
            ret.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left
    return ret
