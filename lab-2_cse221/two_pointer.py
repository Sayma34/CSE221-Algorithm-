def two_sum(total_num, sum, arr):
    left_pointer = 0
    right_pointer = total_num -1
    
    while left_pointer < right_pointer:
        sum_store = arr[left_pointer]+ arr[right_pointer]
        if sum_store == sum:
            print( left_pointer+1 , right_pointer+1)
            return
            
        elif sum_store < sum:
            left_pointer +=1
        else:
            right_pointer+=1
    return -1

total_num, sum = map(int, input().split())

arr = list(map(int, input().split()))
two_sum(total_num, sum, arr)       