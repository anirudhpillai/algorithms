class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [node for i in level for node in [i.left, i.right] if node]
        return ans


# from Queue import deque
#
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if not root:
#             return []
#
#         answer = []
#         curr = deque()
#         nodes = deque()
#
#         curr.append(root)
#         answer.append([root.val])
#
#         while curr:
#             temp = curr.popleft()
#             if temp.left:
#                 nodes.append(temp.left)
#             if temp.right:
#                 nodes.append(temp.right)
#
#             if not curr:
#                 if not nodes:
#                     return answer
#
#                 answer.append(list(map(lambda x: x.val, nodes)))
#                 curr = nodes
#                 nodes = deque()
#
#         return answer
