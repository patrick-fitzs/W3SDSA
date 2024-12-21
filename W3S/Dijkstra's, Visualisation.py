import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]  # Create a matrix to hold all the edges and edge weights
        self.size = size  # Number of vertices in the graph
        self.vertex_data = [''] * size  # Holds the names of all the vertices

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For an undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def visualize(self):
        G = nx.Graph()  # Create an undirected graph

        # Add nodes with labels
        for i, label in enumerate(self.vertex_data):
            G.add_node(i, label=label)

        # Add edges with weights
        for i in range(self.size):
            for j in range(i + 1, self.size):  # Avoid duplicating edges for an undirected graph
                if self.adj_matrix[i][j] != 0:
                    G.add_edge(i, j, weight=self.adj_matrix[i][j])

        # Draw the graph
        pos = nx.spring_layout(G)  # Positions for all nodes
        labels = nx.get_node_attributes(G, 'label')  # Get node labels
        edge_labels = nx.get_edge_attributes(G, 'weight')  # Get edge weights

        nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()


# Creating and populating the graph
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
g.add_edge(2, 6, 7)  # C - G, weight 7
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

# Visualizing the graph
print("\nVisualizing the graph:")
g.visualize()

