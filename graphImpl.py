class Graph:
    def __init__(self, n):
        self.g = [[0]*n for _ in range(n)]

    def addEdge(self, u, v):
        self.g[u][v] = 1

    def display(self):
        for row in self.g:
            print(row)

gr = Graph(4)
gr.addEdge(1, 2)
gr.addEdge(0, 2)
gr.display()    