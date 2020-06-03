import numpy as np

class Graph:

    class Edge:

        def __init__(self, toNode, weigth):
            self.toNode = toNode
            self.weigth = weigth

    class Node:

        def __init__(self, n, value):
            self.value = value
            self.edges = np.zeros(n,dtype=Maze.Edge)

    def __init__(n, p, weigths):
        self.n = n
        self.p = p
        self.nodes = self.edges = np.zeros(n,dtype=Maze.Node)

        #Creating all nodes

        for i in range(self.n):
            self.nodes[i] = Graph.Node(n=self.n,value=1)

        #tie the nods

        for i in range(self.n):
            uniformRange = np.random.uniform(0,1,n)
            print(uniformRange)
            for j in range(self.n):
                if(i == j):
                    self.nodes[i].edges[j] = None
                    continue

                if(self.p >= uniformRange[j]):
                    self.nodes[i].edges[j] = Graph.Edge(self.nodes[j],1)
                else:
                    self.nodes[i].edges[j] = None