graph = {
    "A": ["D", "C", "B"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "G", "H"],
    "E": ["B"],
    "F": ["C", "I", "J"],
    "G": ["D"],
    "H": ["D"],
    "I": ["F"],
    "J": ["F"]
    }

def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while (len(stack) > 0):
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

DFS(graph, "F")
