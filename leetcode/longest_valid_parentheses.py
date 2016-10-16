def longest_valid_parentheses(s):
    stack = []
    start = 0 # this is the start index of a valid parentheses group
    m = 0

    for i in range(len(s)):
        if s[i] == '(': # we push every "("
            stack.append(i)
        else: # if we meet a ")"
            # if the stack is empty, which means all "("s in this valid group have been matched, this group is DONE.
            # we update the new start of the next potential valid group
            if not stack:
                start = i+1
            # if the stack has unmatched "(", which is also the rightmost "(",
            # we pop it out and match with this ")", then we have to update the max length, which has two cases:
            # 1. if the stack is empty, which means all "("s in this valid group have been matched, then the length should be i-start+1.
            # 2. if the stack is not empty, which means we still have unmatched "("s in this group.
            # Then the length should be the length of all matched parentheses so far,
            # the range of which is between the unmatched rightmost "(" [stack.peek()], and the ")" we just met.
            # Remember all "("s and ")"s after stack.peek() have been popped and matched. Thus the length should be i-stack.peek()
            # NOTE: In both case, this group is still valid and not DONE, so we do not need to update the start.
            else:
                stack.pop()
                if not stack:
                    m = max(m, i - start + 1)
                else:
                    m = max(m, i - stack[-1])

    return m

"""
Initial brute force solution

def longestValidParentheses(s):
    m = 0

    for i in range(len(s)):
        l = checkLen(s, i)
        m = max(l, m)

    return m

def checkLen(s, i):
    stack = []
    start = i
    valid = i
    for j in range(i, len(s)):
        if s[j] == '(':
            stack.append('(')
        else:
            if not stack:
                return valid - start
            else:
                stack.pop()
                if not stack:
                    valid = j + 1

    return valid - start
"""
