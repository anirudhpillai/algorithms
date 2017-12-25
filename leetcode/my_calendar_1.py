class Node:
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.tree = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.tree:
            self.tree = Node(start, end)
            return True

        return self.search(start, end, self.tree)

    def search(self, start, end, node):
        if start >= node.end:
            if not node.right:
                node.right = Node(start, end)
                return True
            return self.search(start, end, node.right)
        elif end <= node.start:
            if not node.left:
                node.left = Node(start, end)
                return True
            return self.search(start, end, node.left)
        else:
            return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
