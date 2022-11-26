import sys
import itertools
V=4
INF= sys.maxsize

#Path Matrix
G =  [[0, 7 , INF,8],
      [INF, 0, 5, INF],
      [INF, INF, 0, 2],
      [INF, INF, INF, 0]]

#Function to print solution
def printmatrix(dist):
    print("The followwing shows the shortest path")
    for i in range(V):
      for j in range(V):
        if dist[i][j]==INF:
            print("%7s" % ("INF"), end=" ")
        else:
            print("%7d\t" % (dist[i][j]), end='')
        if j== V-1:
            print()

#Floyd Warshall Algorithm
def floydWarshall(G):
    dist = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k, i, j in itertools.product(range(V), range(V), range(V)):
                #if vertex path is shorter, then update the value
                if(dist[i][j]) > dist[i][k]+dist[k][j]:     
                    dist[i][j] = dist[i][k]+dist[k][j]
    printmatrix(dist)

floydWarshall(G)

#Unit Test
print("\n")
print("Unit Test:")
import unittest
def test_sum():
    assert sum([1,2,3])==6

if __name__ == "__main__":
    test_sum()
    print("Test passed")

