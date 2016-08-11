# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def build_tree(preorder, inorder):
    if not inorder or not preorder:
        return None

    root = TreeNode(preorder[0])
    root_index = inorder.index(preorder[0])

    left, right = inorder[:root_index], inorder[root_index+1:]

    root.left = build_Tree(preorder[1:len(left)+1], left)
    root.right = build_tree(preorder[len(left)+1:], right)
    return root
