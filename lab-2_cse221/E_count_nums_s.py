def binary_search_left(arr, x):
    """Find the leftmost index where arr[index] >= x."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid
        else:
            left = mid + 1
    return left

def binary_search_right(arr, y):
    """Find the rightmost index where arr[index] > y."""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > y:
            right = mid
        else:
            left = mid + 1
    return left

# Read input values
n, q = map(int, input().split())  # Read n (size of array) and q (number of queries)
arr = list(map(int, input().split()))  # Read sorted array

# Process queries
results = []
for _ in range(q):
    x, y = map(int, input().split())

    # Find the lower and upper bounds using manual binary search
    left_index = binary_search_left(arr, x)
    right_index = binary_search_right(arr, y)

    # Count elements in the range [x, y]
    results.append(str(right_index - left_index))

# Print all results at once (faster I/O)
print("\n".join(results))
