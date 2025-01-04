# def matrix(n):
#
#     result = []
#     for i in range(n):
#         result.append([0]*n)
#     return result
#
# matrix1 = matrix(4)
# matrix1[3][1] = 9
#
# for row in matrix1:
#     print(row)
#
vertexData = ['A', 'B', 'C', 'D'] # Vertices / nodes

adjacency_matrix = [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D  All connection for each node
]

def print_adjacency_matrix(matrix):
    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row) # Just printing the matrix

print('vertexData:',vertexData)
print_adjacency_matrix(adjacency_matrix)

def print_connections(matrix, vertices):
    print("\nConnections for each vertex:") # Printing title
    for i in range(len(vertices)):          # iterate over length of vertex data = 4
        print(f"{vertices[i]}: ", end="")   # print each letter
        for j in range(len(vertices)):      # for j in this iteration
            if matrix[i][j]:                # if there is a connection i.e. 1 means connected
                print(vertices[j], end=" ")  #  on the ith line print the index i + j
        print()  # new line

print_connections(adjacency_matrix, vertexData)