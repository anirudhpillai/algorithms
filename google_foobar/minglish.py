def answer(words):
    graph = dict()
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if w1[j] in graph:
                    graph[w1[j]].append(w2[j])
                else:
                    graph[w1[j]] = [w2[j]]
                break

    print(graph)

    stack = []
    visited = set()
    nodes = graph.keys()

    def topsort(vertex):
        if vertex not in visited:
            visited.add(vertex)
            if vertex in graph:
                for i in graph[vertex]:
                    topsort(i)
            stack.append(vertex)

    for i in nodes:
        topsort(i)

    ret = ""

    while stack:
        ret += stack.pop()

    return ret


words = ["a", "ya", "yb", "ba"]

print(answer(words))
