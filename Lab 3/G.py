import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
def build_postorder(in_left, in_right):
    global pre_idx  
    if in_left > in_right:
        return []
 
    root = preorder[pre_idx]
    pre_idx += 1
 
    root_idx = inorder_index[root]
 
    left = build_postorder(in_left, root_idx - 1)
    right = build_postorder(root_idx + 1, in_right)
 
    return left + right + [root]
 
 
n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))
inorder_index = {val: idx for idx, val in enumerate(inorder)}
pre_idx = 0
postorder = build_postorder(0, n - 1)
print(' '.join(map(str, postorder)))