# Step 1: Read number of nodes (N) and edges (M)
N, M = map(int, input().split())

# Step 2: Read M values for u, v, and w
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

# Step 3: Create an empty list for each node (1 to N)
adj_list = []
for i in range(N + 1):  # we add one extra for 1-based indexing
    adj_list.append([])

# Step 4: Add each edge to the list
for i in range(M):
    one_node = u[i]
    another_node = v[i]
    weight = w[i]
    adj_list[one_node].append((another_node, weight))

# Step 5: Print the adjacency list
for i in range(1, N + 1):
    print(str(i) + ":", end="")
    for eg in adj_list[i]:
        print(" (" + str(eg[0]) + "," + str(eg[1]) + ")", end="")
    print()


