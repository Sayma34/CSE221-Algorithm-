# # alice length -- N
# # Bob length -- M
# N = int(input())
# M = int(input())
# def beauty_sort(N, alice_arr, M, bob_arr):
#     
#     right_pointer = 0
    
    
def beauty_sort_list():
    # Read the length of Alice's list
    N_alice = int(input().strip())
    # Read Alice's list
    alice_list = list(map(int, input().strip().split()))
    # Read the length of Bob's list
    M_bob = int(input().strip())
    # Read Bob's list
    bob_list = list(map(int, input().strip().split()))
    
    # Pointers for Alice's and Bob's lists
    left_pointeri = 0
    right_pointerj = 0
    merged_list = []
    
    # Merge the two lists
    while left_pointeri < N_alice and right_pointerj < M_bob:
        if alice_list[left_pointeri] <= bob_list[right_pointerj]:
            merged_list.append(alice_list[left_pointeri])
            left_pointeri += 1
        else:
            merged_list.append(bob_list[right_pointerj])
            right_pointerj += 1
    
    # If there are remaining elements in Alice's list
    while left_pointeri < N_alice:
        merged_list.append(alice_list[left_pointeri])
        left_pointeri += 1
    
    # If there are remaining elements in Bob's list
    while right_pointerj < M_bob:
        merged_list.append(bob_list[right_pointerj])
        right_pointerj += 1
    
    # Print the merged list
    print(" ".join(map(str, merged_list)))

# Example usage:
# Call the function to execute the merging process
beauty_sort_list()