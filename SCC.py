class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.rgraph = [[] for _ in range(num_vertices)]
        self.visited = [False for _ in range(num_vertices)]
        self.finished_vertices = []

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.rgraph[end].append(start)

    def dfs(self, vertex):
        self.visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)
        self.finished_vertices.append(vertex)

    def rdfs(self, vertex, scc):
        self.visited[vertex] = True
        scc.append(vertex)
        for neighbor in self.rgraph[vertex]:
            if not self.visited[neighbor]:
                self.rdfs(neighbor, scc)

    def build_graph(self, edges):
        for start, end in edges:
            self.add_edge(start, end)

    def find_scc(self):
        for vertex in range(self.num_vertices):
            if not self.visited[vertex]:
                self.dfs(vertex)

        self.visited = [False for _ in range(self.num_vertices)]
        print("DFS:", self.finished_vertices)
        self.finished_vertices.reverse()
        print("Reversed DFS:", self.finished_vertices)

        for vertex in self.finished_vertices:
            if not self.visited[vertex]:
                scc = []
                self.rdfs(vertex, scc)
                print(scc)


if __name__ == "__main__":
    edges = [(6,7), (7,5), (5,6), (5,4), (4,3), (3,4), (7,0), (0,3), (3,2), (0,1), (1,0), (0,2), (1,2)]
    g = Graph(8)
    g.build_graph(edges)
    g.find_scc()