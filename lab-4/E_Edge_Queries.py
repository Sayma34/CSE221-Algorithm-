# n, m = map(int, input().split())
# u = list(map(int, input().split()))
# v = list(map(int, input().split()))

# indegree = [0] * (n + 1)
# outdegree = [0] * (n + 1)

# for i in range(m):
#     outdegree[u[i]] += 1
#     indegree[v[i]] += 1

# result = [indegree[i] - outdegree[i] for i in range(1, n + 1)]
# print(" ".join(map(str, result)))


# Step 1: Take input
n, m = map(int, input().split())  # number of nodes and edges

# Step 2: Read the edges
u = list(map(int, input().split()))  # u[i] = starting point of i-th edge
v = list(map(int, input().split()))  # v[i] = ending point of i-th edge

# Step 3: Create two lists to keep track of indegree and outdegree
indegree = [0] * (n + 1)     # list to count arrows coming into each node
outdegree = [0] * (n + 1)    # list to count arrows going out from each node

# Step 4: Count the degrees
for i in range(m):
    outdegree[u[i]] += 1    # this node is the start of an edge
    indegree[v[i]] += 1     # this node is the end of an edge

# Step 5: For each node, calculate indegree - outdegree
result = []
for i in range(1, n + 1):
    result.append(indegree[i] - outdegree[i])

# Step 6: Print the result
print(" ".join(map(str, result)))



# N_node, M_edg = map(int, input().split())
# u = list(map(int, input().split())) 
# v = list(map(int, input().split())) 

# indegree = [0] * (N_node + 1)     
# outdegree = [0] * (N_node + 1)   

# for i in range(M_edg):
#     outdegree[u[i]] += 1
#     indegree[v[i]] += 1 

# result = []
# for i in range(1, N_node + 1):
#     result.append(indegree[i] - outdegree[i])
    
# print(" ".join(map(str, result)))