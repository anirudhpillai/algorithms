def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


class Node:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None


def insert_node(node, key):
    if key > node.key:
        if not node.left:
            node.left = Node(key)
        else:
            insert_node(node.left, key)
    else:
        if not node.right:
            node.right = Node(key)
        else:
            insert_node(node.right, key)


def no_of_nodes(tree):
    if not tree:
        return 0
    else:
        return 1 + no_of_nodes(tree.left) + no_of_nodes(tree.right)


def ans(node):
    if not node:
        return 1

    m = no_of_nodes(node.left)
    n = no_of_nodes(node.right)

    one = (factorial(m+n) / (factorial(m) * factorial(n)))
    return str(int(one * int(ans(node.left)) * int(ans(node.right))))


def answer(seq):
    tree = Node(seq[0])
    for i in range(1, len(seq)):
        insert_node(tree, seq[i])
    return ans(tree)


seq = [5, 9, 8, 2, 1]
print(answer(seq))
