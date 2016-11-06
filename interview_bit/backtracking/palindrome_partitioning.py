class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):

        result = []

        if not A:
            return result

        def is_palindrome(s):
            low, high = 0, len(s)-1
            while low <= high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        # dfs
        def add_palindrome(start, partition):
            if start == len(A):
                result.append(list(partition))
                return

            for i in range(start+1, len(A)+1):
                if is_palindrome(A[start:i]):
                    add_palindrome(i, partition + [A[start:i]])

        add_palindrome(0, [])
        return result
