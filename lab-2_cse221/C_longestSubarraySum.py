def longest_subarr():
    # Read input values
    
    size_arr_N, max_sum_K = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    
    left = 0
    right = 0
    sum = 0
    max_length = 0
    
    for right in range(size_arr_N):
        sum += arr[right]  
        
        # Shrink window from left if sum exceeds K
        if sum > max_sum_K and left <= right:
            sum -= arr[left]
            left += 1
        
        # Update the maximum length of the valid subarray
        if sum <= max_sum_K:
            max_length = max(max_length, right - left + 1)
    
    # Print the result
    print(max_length)

# Example usage:
# Call the function to execute the process
longest_subarr()