from queue import Queue 

#Class for creating Adj Node for Graph
class AdjNode:
    #Initialiser for AdjNode
    def __init__(self,name):
        self.vertice=name
        self.neighbour=[]

#Class for creating and performing operation on Graph
class Graph:

    #Initialiser for Graph
    def __init__(self,vertices):
        self.V= vertices
        print(f"Graph initialized with {len(vertices)} nodes")
    
    #Method for adding Edges
    def addEdge(self,start,destination):
        self.V[start-1].neighbour.append(destination)
        self.V[destination-1].neighbour.append(start)
        print(f"Edge created from {start} to {destination}")

    #Method for printing vertices and its neighbours
    def printGraph(self):
        nodes=self.V
        for i in nodes:
            print(i.vertice,i.neighbour)

    def bfs(self):
        visited=[]
        if(self.V==[]):
            print("No Graph present")
            return
        print("BFS Traversal for current graph is: ")
        while len(visited)!=len(self.V):
            queue = Queue()
            queue.put(self.V[0])
            while(not queue.empty()):
                current_node=queue.get()
                # print(current_node.vertice)
                if(current_node not in visited):
                    print(current_node.vertice,end=" ")
                    visited.append(current_node)
                    for vertices in current_node.neighbour:
                        if(self.V[vertices-1] not in visited):
                            queue.put(self.V[vertices-1])
  

if __name__ == "__main__":
    total_vertices=7
    nodes=[]
    for i in range(1,int(total_vertices)+1):
        node=AdjNode(i)
        nodes.append(node)
    graph=Graph(nodes)
    graph.addEdge(1,2)
    graph.addEdge(1,3)
    graph.addEdge(3,5)
    graph.addEdge(5,6)
    graph.addEdge(6,4)
    graph.addEdge(4,2)
    graph.addEdge(2,7)
    graph.addEdge(6,7)
    graph.printGraph()
    graph.bfs()
    print("\n")