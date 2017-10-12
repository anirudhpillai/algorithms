# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = dict()
        dic[None] = None
        p = head

        while p:
            dic[p] = RandomListNode(p.label)
            p = p.next

        p = head
        while p:
            dic[p].next = dic[p.next]
            dic[p].random = dic[p.random]
            p = p.next

        return dic[head]
