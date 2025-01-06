class NegativeCycle(Exception):
    pass



class GraphNode:
    def __init__(self, id):
        self.id = id
    
    
    def getId(self):
        return self.id



class GraphEdge:
    def __init__(self, firstEndpoint, secondEndpoint, weight):
        self.firstEndpoint = firstEndpoint
        self.secondEndpoint = secondEndpoint
        self.weight = weight
    

    def getFirstEndpoint(self):
        return self.firstEndpoint
    

    def getSecondEndpoint(self):
        return self.secondEndpoint
    

    def getWeight(self):
        return self.weight



class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.graphSize = int(input())
        self.graphArea = self.graphSize * self.graphSize
        self.distances = []
        for i in range(self.graphSize):
            row = []
            self.nodes.append(GraphNode(i))
            self.edges.append([])
            for j in range(self.graphSize):
                row.append(float('inf'))
            self.distances.append(row)
        for num in range(self.graphArea):
            weight = input()
            if (weight.lstrip("-").isnumeric()):
                self.distances[num // self.graphSize][num % self.graphSize] = int(weight)
                if (weight != 0):
                    edge = GraphEdge(self.nodes[num // self.graphSize], self.nodes[num % self.graphSize], int(weight))
                    self.edges[num // self.graphSize].append(edge)
        self.bellmanFord()
        self.displayMatrix()


    def bellmanFord(self):
        for i in range(self.graphSize):
            try:
                for j in range(self.graphSize - 1):
                    for edges in self.edges:
                        for edge in edges:
                            oldDistance = self.distances[i][edge.getFirstEndpoint().getId()]
                            otherNodeId = edge.getSecondEndpoint().getId()
                            otherDistance = self.distances[i][otherNodeId]
                            if (oldDistance != float('inf')) and (oldDistance + edge.getWeight() < otherDistance):
                                self.distances[i][otherNodeId] = oldDistance + edge.getWeight()
                
                for j in range(self.graphSize - 1):
                    for edges in self.edges:
                        for edge in edges:
                            oldDistance = self.distances[i][edge.getFirstEndpoint().getId()]
                            otherNodeId = edge.getSecondEndpoint().getId()
                            otherDistance = self.distances[i][otherNodeId]
                            if (oldDistance != float('inf')) and (oldDistance + edge.getWeight() < otherDistance):
                                raise NegativeCycle
            except NegativeCycle:
                self.distances[i] = [None] * self.graphSize
                continue


    def displayMatrix(self):
        for i in range(self.graphSize):
            str = f"Node {i}: {self.distances[i]}"
            print(str)



Graph()