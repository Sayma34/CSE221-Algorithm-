#E. Ordering Binary Tree
def build_bst(arr, left, right, rslt):
  if left>right:
    return
  mid=(left+right)//2
  rslt.append(arr[mid])
  build_bst(arr, left, mid-1, rslt)
  build_bst(arr, mid+1, right, rslt)

def bst_height(N, arr):
  rslt=[]
  build_bst(arr, 0, N-1, rslt)
  return rslt

N=int(input().strip())
arr=list(map(int, input().strip().split()))
rslt=bst_height(N, arr)
print(" ".join(map(str, rslt)))