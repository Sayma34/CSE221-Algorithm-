def merge_and_count(arr, temp_arr, left, mid, right):
    i = left    # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left  # Starting index for merged array
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # Count the inversions
            j += 1
        k += 1

    while i <= mid:  # Copy remaining elements from left subarray
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:  # Copy remaining elements from right subarray
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):  # Copy sorted elements back to original array
        arr[i] = temp_arr[i]
    
    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions_and_sort(arr, n):
    temp_arr = [0] * n
    inv_count = merge_sort_and_count(arr, temp_arr, 0, n - 1)
    print(inv_count)
    for num in arr:
        print(num, end=" ")
    print()

# Read input
n = int(input())
arr = list(map(int, input().split()))
temp_arr = [0] * n
inv_count = merge_sort_and_count(arr, temp_arr, 0, n - 1)
print(inv_count)
for num in arr:
    print(num, end=" ")
print()
