"""
Floyd-Warshall algorithm
In the function fw(M),
implement the Floyd-Warshall algorithm for an unweighted adjacency matrix M.
After the function has finished,
the matrix should have M[i][j] == 1 whenever it is possible to travel from i to j along any number of edges of the matrix.
(This includes the diagonal: we should also have M[i][i] == 1 for all i because technically,
 you can always "get from i to i" by doing nothing.)
You may wish to display the matrix M after each step of the process,
to check it is working correctly. For this you can use the show(M) function provided.

"""

def show(M):
    print("\n".join(map(str, M)))

def fw(M):
    n = len(M)
    for i in range(n):
    # update M as described in the lecture slides
    # Each iteration should update M to be M0, then M1, ..., up to M_(n-1).
        M[i][i] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if M[i][k] == 1 and M[k][j] ==1:
                    M[i][j] = 1
        print(f"After including node {k}:")
        show(M)
        print()

M = [
  [0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0],
]

print("After fw(M), M should all be 1s:")
fw(M)
show(M)
