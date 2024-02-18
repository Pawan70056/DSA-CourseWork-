import heapq

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self, V):
        self.adjList = [[] for _ in range(V)]

    def addEdge(self, src, dest, weight):
        self.adjList[src].append(Edge(src, dest, weight))
        self.adjList[dest].append(Edge(dest, src, weight))  # Undirected graph

    def kruskalMST(self):
        pq = []
        parent = [i for i in range(len(self.adjList))]
        rank = [0] * len(self.adjList)

        # Add all edges to the priority queue (min heap)
        for edges in self.adjList:
            for edge in edges:
                heapq.heappush(pq, edge)

        mst = []
        # Process edges until we have V-1 edges (all vertices connected)
        while pq and len(mst) < len(self.adjList) - 1:
            edge = heapq.heappop(pq)
            x = self.find(parent, edge.src)
            y = self.find(parent, edge.dest)
            # Check for cycle formation
            if x != y:
                mst.append(edge)
                self.union(parent, rank, x, y)

        return mst

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        # Attach smaller tree under root of larger tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

if __name__ == "__main__":
    graph = Graph(4)
    graph.addEdge(0, 1, 10)
    graph.addEdge(0, 2, 6)
    graph.addEdge(0, 3, 5)
    graph.addEdge(1, 2, 4)
    graph.addEdge(2, 3, 8)
    mst = graph.kruskalMST()
    print("Minimum Spanning Tree Edges:")
    for edge in mst:
        print(f"{edge.src} - {edge.dest} ({edge.weight})")


