import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
def build_preorder(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return []
    root = postorder[post_right]
    root_idx = inorder_index[root]
    left_size = root_idx - in_left
    left_pre = build_preorder(in_left, root_idx - 1, post_left, post_left + left_size - 1)
    right_pre = build_preorder(root_idx + 1, in_right, post_left + left_size, post_right - 1)
 
    return [root] + left_pre + right_pre
 
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_index = {val: idx for idx, val in enumerate(inorder)}
preorder = build_preorder(0, n - 1, 0, n - 1)
print(' '.join(map(str, preorder)))