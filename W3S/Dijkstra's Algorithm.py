from networkx.algorithms.shortest_paths.unweighted import predecessor


class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]  # create a matrix to hold all the edges and edge weights
        self.size = size # number of vertices in the graph
        self.vertex_data = [''] * size # holds the names of al the vertices

    def add_edge(self, u, v, weight):
        if 0 <= u <= self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight # Just this line for a directed graph
            self.adj_matrix[v][u] = weight # for an undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <=vertex <self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        # sets a start vertex , in this case i = 3 = 'D'
        start_vertex = self.vertex_data.index(start_vertex_data)

        # if you want to stop at a certain vertex
        # end_vertex = self.vertex_data.index(end_vertex_data) # add End_vertex_data into this functions arguments

        # creates a distance list with size of graph, all initialised to inf
        # distances = [inf, inf, inf, 0, inf, inf, inf]
        distances = [float('inf')] * self.size

        # create an array to hold previously visited
        predecessors = [None] * self.size

        # distance with itself is always 0
        distances[start_vertex] = 0

        # create a visited list, initialised to false for all
        # visited = [False, False, False, False, False, False, False]
        visited = [False] * self.size

        # loops self.size times, in this case 7
        for _ in range(self.size):

            # find the closest unvisited vertex
            min_distance = float('inf')

            # sets current node to none, i.e. first node A is now none
            u = None

            for i in range(self.size):
                # if A is false(not visited yet) and 4 < inf
                if not visited[i] and distances[i] < min_distance:
                    # the min distance is now 4 ^^
                    min_distance = distances[i]
                    # u or current node is now 4, A = 4 , distance from D to A
                    u = i

            ### this change for stopping at a certain vertex ###
            # if u is None or u == end_vertex:
            #     print(f"Breaking out of loop. Current vertex: {self.vertex_data[u]}")
            #     print(f"Distances: {distances}")
            #     break
            # if no unvisited nodes are reachable, terminate
            if u is None:
                break

            # mark the node we just visited as true to state its been visited
            visited[u] = True

            for v in range(self.size):
                # check there's an edge between u and v(current and neighbour node)
                # and ensures it's not been visited yet
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    # calculates alt distances to v(neighbour) through u(current)
                    alt = distances[u] + self.adj_matrix[u][v]
                    # if this alt distance is shorter than known distance, update
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u

        return distances, predecessors

    # function for storing and showing the path to each vertex
    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)  # Join the vertices with '->'


g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

# Dijkstra's algorithm from D to all vertices
print("\nDijkstra's Algorithm starting from vertex D:")
distances, predecessors = g.dijkstra('D')
for i, d in enumerate(distances):
    path = g.get_path(predecessors, 'D', g.vertex_data[i])
    print(f"{path}, Distance: {d}")