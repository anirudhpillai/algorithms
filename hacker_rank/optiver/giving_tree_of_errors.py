import re


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_input_valid(inp):
    pairs = inp.split()

    if not pairs:
        return "E1"

    for pair in pairs:
        if len(pairs) != 5:
            return "E1"

        check = (
            pairs[0] == "(" and
            pairs[4] == ")" and
            pairs[1].isalpha() and
            pairs[3].isalpha()
        )

        if not check:
            return False

    return True

def build_tree(inp):
    # check input here
    err = is_input_valid(inp)
    if not err:
        return "E1"


    letter_to_node = {}
    has_parent = {}

    pairs = inp.split()
    for pair in pairs:
        parent, child = pair[1], pair[3]

        if child in has_parent and has_parent[child] == parent:
            return "E2"  # duplicate pair

        has_parent[child] = parent

        if child in letter_to_node:
            child_node = letter_to_node[child]
        else:
            child_node = Node(child)
            letter_to_node[child] = child_node

        if parent in letter_to_node:
            parent_node = letter_to_node[parent]
            if not parent_node.left:
                parent_node.left = child_node
            elif parent_node.right:
                return "E3"  # parent has more than 2 children
            else:
                if parent_node.left.val > child_node.val:
                    parent_node.right = parent_node.left
                    parent_node.left = child_node
                else:
                    parent_node.right = child_node
        else:
            parent_node = Node(parent)
            letter_to_node[parent] = parent_node
            parent_node.left = child_node

    roots = list(set(letter_to_node.keys()) - set(has_parent.keys()))
    if len(roots) > 1:
        return "E5" # has multiple roots

    parent = roots[0]

    visited = {}

    def serialise_tree(root):
        if not root:
            return ""

        if root.val in visited:
            raise Exception("Tree has cycles")  # tree has cycle

        visited[root.val] = True

        result = (
            "("
            + root.val
            + serialise_tree(root.left)
        )

        if not root.right:
            result += ")"
        else:
            result += (
                " "
                + serialise_tree(root.right)
                + ")"
            )

        return result

    try:
        answer = serialise_tree(letter_to_node[parent])
    except:
        return "E4" # tree has cycle
    
    return answer


assert build_tree("(A,B) (B,C) (A,E) (B,D)") == "(A(B(C) (D)) (E))"
assert build_tree("(A,B) (A,C) (B,D) (D,C)") == "E4"
assert build_tree("(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)") == "(A(B(D(E(G)))) (C(F)))"
assert build_tree("(A,B) (A,C) (B,D) (D,C)") == "E4"
assert build_tree("(A,C) (A,B) (B,Q) (B,P) (C,D) (Q,Z) (Q,X)").replace(" ", "") == "(A(B(P)(Q(X)(Z)))(C(D)))"
