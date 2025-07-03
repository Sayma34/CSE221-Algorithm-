# Step 1: Read input
N_nodes, M_edges, S, D = map(int, input().split())  # n = number of nodes, m = number of edges, s = source, d = destination

# Step 2: Initialize adjacency list
adj = []
for i in range(N_nodes + 1):  # node numbering starts from 1 to N
    adj.append([])  # create empty list for each node

# Step 3: Read edges
u = list(map(int, input().split()))
v = list(map(int, input().split()))

# Step 4: Build the undirected graph
for i in range(M_edges):
    X = u[i]
    Y = v[i]
    adj[X].append(Y)  # add b to a's neighbors
    adj[Y].append(Y)  # add a to b's neighbors

# Step 5: Sort neighbors to ensure lexicographically smallest path
for i in range(1, N_nodes + 1):
    adj[i].sort()

# Step 6: Initialize BFS structures
from collections import deque
visited = [False] * (N_nodes + 1)  # mark visited nodes
dist = [-1] * (N_nodes + 1)        # distance from source
parent = [-1] * (N_nodes + 1)      # to trace back the path

# Step 7: BFS from source 's'
q = deque()
q.append(S)
visited[S] = True
dist[S] = 0

while q:
    node = q.popleft()

    for nihbr in adj[node]:
        if not visited[nihbr]:
            visited[nihbr] = True
            dist[nihbr] = dist[node] + 1
            parent[nihbr] = node
            q.append(nihbr)

# Step 8: Check if destination is reachable
if dist[D] == -1:
    print(-1)
else:
    print(dist[D])  # number of edges from source to destination

    # Step 9: Reconstruct the path from destination to source using parent array
    path = []
    curr = D
    while curr != -1:
        path.append(curr)
        curr = parent[curr]

    # Step 10: Reverse the path and print it
    path.reverse()
    print(*path)
