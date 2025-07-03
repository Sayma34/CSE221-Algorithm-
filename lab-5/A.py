# Step 1: Read the first line: number of nodes (n) and edges (m)
N_cities, M_roads = map(int, input().split())

# Step 2: Create an adjacency list for the graph
# We use n+1 because nodes are from 1 to n (index 0 will remain unused)
adj = [] 
for i in range(N_cities + 1):
    adj.append([])

# Step 3: Read the edges and build the adjacency list
for i in range(M_roads):
    u, v = map(int, input().split())
    # Since the graph is undirected, add both directions
    adj[u].append(v)
    adj[v].append(u)

# Step 4: Prepare for BFS
visited = [False] * (N_cities + 1)  # Track visited nodes
queue = []                   # Queue to hold nodes to visit
ord = []                   # To store the BFS traversal order

# Step 5: Start BFS from node 1
queue.append(1)
visited[1] = True  # Mark node 1 as visited

# Step 6: Perform BFS
while queue:
    curr = queue.pop(0)  # Dequeue
    ord.append(curr)   # Add to output
    
    # Visit all unvisited neighbors
    for nihbr in adj[curr]:
        if not visited[nihbr]:
            visited[nihbr] = True  # Mark as visited
            queue.append(nihbr)    # Enqueue

# Step 7: Print the BFS traversal order
for node in ord:
    print(node, end=' ')
