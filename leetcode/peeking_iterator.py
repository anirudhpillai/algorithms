class PeekingIterator(object):
    """
    This solution caches the next element
    This problem can also be solved by instantiating a queue
    """
    def __init__(self, iterator):
        self.iter = iterator
        self.temp = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.temp

    def next(self):
        ret = self.temp
        self.temp = self.iter.next() if self.iter.hasNext() else None
        return ret

    def hasNext(self):
        return self.temp is not None
