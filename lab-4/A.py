
# Read the number of nodes and edges
N, M = map(int, input().split())

# Initialize the adjacency matrix with zeros
#adj_matrix = [[0] * N for _ in range(N)]
adj_mat = []
for i in range(N):
    rows = [0] * N
    adj_mat.append(rows)

# Read each edge and populate the adjacency matrix
for i in range(M):
    u, v, w = map(int, input().split())
    adj_mat[u - 1][v - 1] = w  # Set the weight in the matrix

# Output the adjacency matrix
for rows in adj_mat:
    print(' '.join(map(str, rows)))