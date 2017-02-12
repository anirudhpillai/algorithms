class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        O(n) using stack and being greedy
        I could've used 26 char array but this is neater I think
        """

        count = dict()
        for i in s:
            count[i] = count.get(i, 0) + 1

        stack = []
        added = dict()

        for i in s:
            count[i] -= 1

            # if it is already in stack
            if i in added:
                continue

            while stack:
                curr = stack[-1]
                # remove things from stack as long as everything before i
                # is less that i and has atleast one occurence after i in s
                if ord(curr) < ord(i) or count[curr] == 0:
                    break
                stack.pop()
                del added[curr]

            stack.append(i)
            added[i] = True

        return "".join(stack)
