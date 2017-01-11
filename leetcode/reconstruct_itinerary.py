def findItinerary(tickets):
    mp = {}

    for arr, dep in tickets:
        if arr in mp:
            mp[arr].append(dep)
        else:
            mp[arr] = [dep]

    result = ["JFK"]

    def rec(curr):
        last = curr[-1]

        if last not in mp or not mp[last]:
            if len(curr) == len(tickets)+1:
                return curr
            else:
                return None

        val = mp[last]
        for i in sorted(val):
            mp[last].remove(i)
            ans = rec(curr+[i])
            if ans:
                return ans
            mp[last].append(i)


    return rec(result)

print(findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
