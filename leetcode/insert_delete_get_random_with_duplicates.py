import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.indices = {}
        self.vals = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            self.indices[val].append(len(self.vals))
            self.vals.append(val)
            return True
        else:
            self.indices[val] = [len(self.vals)]
            self.vals.append(val)
            return False
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indices and self.indices[val]:
            idx = self.indices[val].pop()
            
            if idx == len(self.vals) - 1:
                self.vals.pop()
            else:
                last_val = self.vals.pop()
                self.vals[idx] = last_val
                self.indices[last_val].remove(len(self.vals))
                self.indices[last_val].append(idx)
                
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.vals)
