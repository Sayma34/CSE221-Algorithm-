def max_squared_sum(arr, left, right):
    if left == right:
        return float('-inf')
        #return -1

    mid = (left + right) // 2

    # Recursively find max squared sum in left and right halves
    left_max = max_squared_sum(arr, left, mid)
    right_max = max_squared_sum(arr, mid + 1, right)

    # Find the two largest numbers in the left half
    left1 = left2 = float('-inf')
    for i in range(left, mid + 1):
        if arr[i] > left1:
            left2, left1 = left1, arr[i]
        elif arr[i] > left2:
            left2 = arr[i]

    # Find the two largest numbers in the right half
    right1 = right2 = float('-inf')
    for i in range(mid + 1, right + 1):
        if arr[i] > right1:
            right2, right1 = right1, arr[i]
        elif arr[i] > right2:
            right2 = arr[i]

    # Compute max squared sum using best pairs
    cross_max = max((left1 + right1) ** 2, (left1 + right2) ** 2, (left2 + right1) ** 2)

    return max(left_max, right_max, cross_max)

# Driver Code
N = int(input())
arr = list(map(int, input().split()))
print(max_squared_sum(arr, 0, N - 1))
#print(max_squared_sum(N,A))
