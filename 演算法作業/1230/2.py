class DisjointSet(dict):

    def __init__(self, dict):
        pass

    def add(self, item):
        self[item] = item

    def find(self, item):
        if self[item] != item:
            self[item] = self.find(self[item])
        return self[item]

    def unionset(self, item1, item2):
        self[item2] = self[item1]

def Kruskal(nodes, edges):
    all_nodes = nodes
    used_nodes = set()
    MST = []
    edges = sorted(edges, key=lambda element: element[2], reverse=True)
    while used_nodes != all_nodes and edges:
        element = edges.pop(-1)
        if element[0] in used_nodes and element[1] in used_nodes:
            continue
        MST.append(element)
        used_nodes.update(element[:2])
    return MST


def main():
    nodes = set(list('ABCDEF'))
    edges = [("A", "B", 6), ("A", "E", 10),
             ("A", "F", 12), ("B", "C", 3),
             ("B", "D", 5), ("B", "F", 8),
             ("C", "D", 7), ("D", "E", 9),
             ("D", "F", 11), ("E", "F", 16)]

    print("The minimum spanning tree by Kruskal is : ")
    print(Kruskal(nodes, edges))


if __name__ == '__main__':
    main()
