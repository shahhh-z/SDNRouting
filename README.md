# sdnRouting
Determines shortest routes to hosts using Bellman-Ford's algorithm.

How to run:
Download the program and open it in an IDE. Run it and pass the information (first pass the dimensions of the NxN adjacency matrix then pass the costs of each connection). The program will output the shortest distances to each host in the network.

Example:
# INPUT MATRIX
0    4    3    inf  inf	
inf  0    -1   1    2
inf  inf  0    5    inf
inf  inf  inf  0    -3
inf  inf  inf  inf  0

# OUTPUT
Node 0: [0, 4, 3, 5, 2]
Node 1: [inf, 0, -1, 1, -2]
Node 2: [inf, inf, 0, 5, 2]
Node 3: [inf, inf, inf, 0, -3]
Node 4: [inf, inf, inf, inf, 0]

NOTE: Use f when inputting infinity.
