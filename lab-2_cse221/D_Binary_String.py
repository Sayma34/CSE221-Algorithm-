Test_case_nmbr = int(input().strip())


def find_one(bin_str):
    left = 0
    right = len(bin_str)-1
    found_one = -1
    for var in range(len(bin_str)):
        if left <= right:
            mid = (left + right)//2
            if bin_str[mid] == '1':
                found_one = mid+1
                right = mid -1
            else:
                left = mid+1
    return found_one

store = []
for i in range(Test_case_nmbr):
    
      bin_str = input().strip()
     #print(find_one(bin_str))
      store.append(str(find_one(bin_str)))
print("\n".join(store))
                
                