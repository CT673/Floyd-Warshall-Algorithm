import sys
import itertools

INF = sys.maxsize
Graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]
# Define the length of graph
V = len(Graph[0])
# Copy of G
dist = list(map(lambda i: list(map(lambda j: j, i)), Graph))


# Introducing individual vertex
def paths():
    """Recursive way to find the shortest path between nodes"""
    def floyd(i, j, k,):
        if i < V and j < V and k < V:  # Base case; checked for 64times; reset all vertices
            dist[i][j] = min(dist[i][j]), dist[i][k] + dist[k][j]   # Final result
            floyd(k, i, j)
        elif j < V and k < V:    # Recursive case; checked 16 times; reset j, k
            dist[i][j] = min(dist[i][j]), dist[i][k] + dist[k][j]   # Final result
            floyd(k, i, j)
        elif k < V:              # Recursive case 2; checked 4 times; reset i , j
            i, j = 0, 0
            dist[i][j] = min(dist[i][j]), dist[i][k] + dist[k][j]   # Final result
            floyd(i, j, k)
        printmatrix()

    # Print output
    def printmatrix():
        print("The output of the shortest path")
        for i in range(V):
            for j in range(V):
                if dist[i][j] == INF:
                    print("%7s" % "INF", end=" ")
                else:
                    print("%7d\t" % (dist[i][j]), end='')
                if j == V - 1:
                    print()
        print()

    # Output of the shortest path
    printmatrix()


paths()
