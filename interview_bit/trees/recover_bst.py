def answer(root):
    arr = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        arr.append(node.val)
        inorder(node.right)
    inorder(root)
    prev = -1
    for i in arr:
        if i < prev:
            ans.append(i)
            ans.append(prev)
        prev = i
    if len(ans) == 2:
        return ans
    else:
        return list(reversed(ans[1:3]))
