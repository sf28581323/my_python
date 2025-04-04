def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex", v, "already exists.")
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no >1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)

def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    if v1 not in vertices:
        print("Vertex", v1, "does not exist.")
    elif v2 not in vertices:
        print("Vertex", v2, "does not exist.")
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

vertices = []
vertices_no = 0
graph = []
add_vertex("A")
add_vertex("B")
add_vertex("C")
add_edge('A', 'B', 5)
add_edge('A', 'C', 6)
add_edge('B', 'A', 10)
add_edge('C', 'A', 3)
add_edge('C', 'B', 2)
print(graph)
