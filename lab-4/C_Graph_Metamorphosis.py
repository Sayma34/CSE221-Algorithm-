# Step 1: Read number of vertices
int_N = int(input())

# Step 2: Create N x N matrix filled with 0
adj_matrix = []
for i in range(int_N):
    adj_matrix.append([0] * int_N)

# Step 3: Read adjacency list and fill the matrix
for i in range(int_N):
    values = list(map(int, input().split()))
    k = values[0]
    neighbors = values[1:]
    for j in neighbors:
        adj_matrix[i][j] = 1

# Step 4: Print the matrix
for row in adj_matrix:
    print(' '.join(map(str, row)))
