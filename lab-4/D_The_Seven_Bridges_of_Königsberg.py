# Step 1: Read number of nodes and edges
N_vert= map(int, input().split())
M_edg = map(int, input().split())

# Step 2: Read endpoints of all edges
u = list(map(int, input().split()))  # First endpoints of edges
v = list(map(int, input().split()))  # Second endpoints of edges

# Step 3: Initialize degree array with zeros (1-based indexing)
degree = [0] * (N_vert + 1)

# Step 4: Count degree for each node by visiting all edges
for i in range(M_edg):
    degree[u[i]] += 1   # Increase degree of node u[i]
    degree[v[i]] += 1   # Increase degree of node v[i] (because undirected)

# Step 5: Count how many nodes have odd degree
count = 0
for i in range(1, N_vert + 1):
    if degree[i] % 2 == 1:
        count += 1

# Step 6: Check Eulerian Path condition
if count == 0 or count == 2:
    print("YES")
else:
    print("NO")
