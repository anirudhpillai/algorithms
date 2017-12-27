def diff(ai, bi):
    if len(ai) != len(bi):
        return -1

    map_ai, map_bi = {}, {}
    for i in range(len(ai)):
        map_ai[ai[i]] = 1 + map_ai.get(ai[i], 0)
        map_bi[bi[i]] = 1 + map_bi.get(bi[i], 0)


    print(map_ai)
    print(map_bi)

    result = 0

    for k, v in map_ai.items():
        if map_bi.get(k, 0) <= v:
            print(k, v, map_bi.get(k, 0))
            result += abs(v - map_bi.get(k, 0))

    return result

print(diff("hhpddlnnsjfoyxpci", "ioigvjqzfbpllssuj"))



visited = {}
queue = []
queue.append(source)

visited[source] = True

while queue:
    current = queue.pop()
    if current == dest:
        return True

    for node in graph[current]:
        if node not in visited:
            queue.append(i)
            visited[node] = True

return False

        # Create a queue for BFS
        queue=[]

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            #Dequeue a vertex from queue
            n = queue.pop(0)

            # If this adjacent node is the destination node,
            # then return true
            if n == d:
                return True

            #  Else, continue to do BFS
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        # If BFS is complete without visited d
        return False
