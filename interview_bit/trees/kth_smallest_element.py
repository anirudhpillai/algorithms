# iterative solution
def kthsmallest(root, k):
    stack = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            t = stack.pop()
            k -= 1
            if k == 0:
                return t.val
            root = t.right

    return None

# recursive solution
def kthsmallest(root, k):

    def find(root, k):
        if not root:
            return (None, k)
        k1 = self.find(root.left, k)
        k = k1[1]
        if k == 0:
            return (k1[0], 0)
        k -= 1
        if k == 0:
            return (root.val, 0)
        return self.find(root.right, k)

    return find(root, k)[0]
