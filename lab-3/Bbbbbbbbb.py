def pair_sq_sum(arr):
    N = len(arr)
    if N<=1:
        return -float("inf")
    mid = N//2
    left_max = pair_sq_sum(arr[:mid])
    right_max = pair_sq_sum(arr[mid : ])
    
    cross_max = -float("inf")
    for i in range(mid):
        for j in range(mid, N):
            cross_max = max(cross_max, arr[i]+arr[j]**2)
    return max(left_max, right_max, cross_max)

N = int(input())
arr = list(map(int,input().split()))
result = pair_sq_sum(arr)
print(result)
