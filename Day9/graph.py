class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
    def printGraph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def removeEdge(self, v1, v2):
        if v1 in self.adjacency_list and v2 in self.adjacency_list:

            if v2 in self.adjacency_list[v1]:
                self.adjacency_list[v1].remove(v2)

            if v1 in self.adjacency_list[v2]:
                self.adjacency_list[v2].remove(v1)

    def removeVertex(self, vertex):
        for otherVertex in self.adjacency_list[vertex]:
            self.adjacency_list[otherVertex].remove(vertex)


my_graph = Graph()
my_graph.addVertex("A")
my_graph.addVertex("B")
my_graph.addVertex("C")
my_graph.addVertex("D")
my_graph.addVertex("E")

my_graph.addEdge("A","B")
my_graph.addEdge("A","C")
my_graph.addEdge("A","D")

my_graph.addEdge("B","A")
my_graph.addEdge("B","E")

my_graph.addEdge("C","A")
my_graph.addEdge("C","D")

my_graph.addEdge("D","A")
my_graph.addEdge("D","C")
my_graph.addEdge("D","E")

my_graph.addEdge("E","B")
my_graph.addEdge("E","D")

my_graph.printGraph()
my_graph.removeVertex("C")
my_graph.printGraph()