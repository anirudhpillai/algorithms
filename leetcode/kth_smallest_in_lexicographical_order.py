# you can't generate all no. upto k, that's TLE
# you'll have to skip through no.


class Solution(object):
    def findKthNumber(self, n, k):
        # counts lexicograpically generated numbers
        # between c and n
        def count(c, n):
            ans, s, e = 0, c, c+1
            while s <= n:
                ans += min(n+1, e) - s
                s *= 10
                e *= 10
            return ans

        curr = 1

        # narrowing the angle
        # if k in 1, 10, 100...
        # then look into it
        # otherwise try 2, 20, 200...
        while k > 1:
            cnt = count(curr, n)
            if cnt < k:
                k -= cnt
                curr += 1
            else:
                curr *= 10
                k -= 1

        return curr


# My TLE Solution
# def next_int(a):
#     if a*10 <= n:
#         return a*10
#     else:
#         if int(str(a)+'0') <= n:
#             return int(str(a)+'0')

#         a = str(a)
#         for i in range(len(a)-1, -1, -1):
#             if a[i] != '9':
#                 ans = int(a[:i] + str(int(a[i])+1))
#                 if ans <= n:
#                     return ans

#         return -1

# ret = 1
# for i in range(k-1):
#     ret = next_int(ret)

# return ret
