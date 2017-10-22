class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        input = path.split("/")
        stack = []

        for dir in input:
            if not dir or dir == ".":
                continue
            if dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return "/" + "/".join(stack)
