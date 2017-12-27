class Solution:
    def deleteNode(self, root, key):
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            lcs = root.right
            while lcs.left:
                lcs = lcs.left

            self.deleteNode(root, lcs.val)
            lcs.right = root.right
            lcs.left = root.left
            return lcs

        return root
