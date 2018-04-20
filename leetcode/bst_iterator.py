class BSTIterator(object):
    def __init__(self, root):
        """
        Beats 95.12%
        """
        self.stack = []
        temp = root
        
        while temp:
            self.stack.append(temp)
            temp = temp.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return
        
        top = self.stack.pop()
        
        temp = top.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        
        return top.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
