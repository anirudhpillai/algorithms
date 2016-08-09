# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def sorted_array_to_bst(arr):
    if not arr:
        return None
    return helper(arr, 0, len(arr) - 1);

def helper(arr, low, high):
    if low > high:
        return None
    mid = (low + high)/2
    node = TreeNode(arr[mid])
    node.left = helper(arr, low, mid - 1)
    node.right = helper(arr, mid + 1, high)
    return node
