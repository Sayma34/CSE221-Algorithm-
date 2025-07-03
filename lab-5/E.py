# Step 1: Take input values
N, M = map(int, input().split())  # n = number of nodes, m = number of edges

# Step 2: Build the adjacency list
adj = []
for i in range(N + 1):  # index 1 to n
    adj.append([])

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)  # directed edge from u to v

# Step 3: Initialize color array
# 0 = unvisited, 1 = visiting, 2 = visited
clr = []
for i in range(N + 1):
    clr.append(0)

# Step 4: Flag to track if a cycle is found
cycl_found = [False]  # use list to modify inside dfs

# Step 5: DFS function to detect cycle
def dfs(u):
    if cycl_found[0]:  # early exit if cycle is already found
        return

    clr[u] = 1  # mark node as visiting

    for v in adj[u]:
        if clr[v] == 0:  # if not visited, visit it
            dfs(v)
        elif clr[v] == 1:  # found a back edge → cycle
            cycl_found[0] = True
            return

    clr[u] = 2  # mark node as fully visited

# Step 6: Run DFS from all unvisited nodes
for i in range(1, N + 1):
    if clr[i] == 0:
        dfs(i)
    if cycl_found[0]:  # break early if cycle detected
        break

# Step 7: Output result
if cycl_found[0]:
    print("YES")
else:
    print("NO")
