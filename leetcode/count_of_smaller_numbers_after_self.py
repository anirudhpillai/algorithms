class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.left_nodes_count = 0
        self.count = 1


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        def insert(x, node, current_count):
            if x < node.val:
                node.left_nodes_count += 1
                if not node.left:
                    node.left = Node(x)
                else:
                    return insert(x, node.left, current_count)
            elif x > node.val:
                current_count += node.count + node.left_nodes_count
                if not node.right:
                    node.right = Node(x)
                else:
                    return insert(x, node.right, current_count)
            else:
                current_count += node.left_nodes_count
                node.count += 1
            return current_count

        root = Node(nums[-1])
        result = [0]

        for i in reversed(nums[:-1]):
            count = insert(i, root, 0)
            result.append(count)

        return result[::-1]
