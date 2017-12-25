class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        level_order = []
        current_level = [root]

        while current_level:
            next_level = [node.left for node in current_level if node.left] + [node.right for node in current_level if node.right]
            level_order.append(current_level[::])
            current_level = next_level

        return list(map(lambda level: sum(map(lambda x: x.val, level)) / len(level), level_order))


"""
@awice's solution using dfs
This is how you can solve it using recursion

def averageOfLevels(self, root):
    info = []
    def dfs(node, depth = 0):
        if node:
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
    dfs(root)

    return [s/float(c) for s, c in info]
"""
