# Python Program for Floyd Warshall Algorithm

def floydmain():
    # Number of vertices in the graph
    V = 4
    INF = 99999

    def floydWarshall(graph):
        dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
        for k in range(V):

            # pick all vertices as source one by one
            for i in range(V):

                # Pick all vertices as destination for the
                # above picked source
                for j in range(V):
                    # If vertex k is on the shortest path from
                    # i to j, then update the value of dist[i][j]
                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j]
                                     )
        printSolution(dist)

    # A utility function to print the solution
    def printSolution(dist):
        for i in range(V):
            for j in range(V):
                if (dist[i][j] == INF):
                    print("%7s" % ("INF"), end=" ")
                else:
                    print("%7d" % (dist[i][j]), end=' ')
                if j == V - 1:
                    print()
        print()

    # Driver program to test the above program
    # Let us create the following weighted graph
    """
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           """
    graph = [
        [0, 7, INF, 8],
        [INF, 0, 5, INF],
        [INF, INF, 0, 2],
        [INF, INF, INF, 0]
    ]
    # Print the solution
    floydWarshall(graph)


# This code is contributed by Mythri J L
floydmain()

