# improved solution
def generateParenthesis(n):
    all = []

    def dfs(curr, l, r):
        if l > r:
            return

        if l == 0 and r == 0:
            all.append(curr)
            return

        if l > 0:
            dfs(curr + "(", l - 1, r)

        if r > 0:
            dfs(curr + ")", l, r-1)

    dfs("", n, n)
    return all


""" Initial Solution

def generateParenthesis(n):
    all = []

    def generate(curr, l, r):
        if l == 0:
            if r == 0:
                all.append(curr)
            else:
                generate(curr + ')', l, r - 1)
        else:
            if l == r:
                generate(curr + '(', l - 1, r)
            else:
                generate(curr + '(', l - 1, r)
                generate(curr + ')', l, r - 1)

    generate("", n, n)

    return all
"""


print(generateParenthesis(3))
