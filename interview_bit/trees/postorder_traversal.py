# recursive
def postorder_recursive(root):
        values = []

        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            traverse(root.right)
            values.append(root.val)

        traverse(root)
        return values
        
# iterative
def postorder_iterative(root):
    postorder = []
    stack1 = []
    stack2 = []

    if not root:
        return None

    stack1.append(root)

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.push(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        postorder.append(node.val)

    return postorder
