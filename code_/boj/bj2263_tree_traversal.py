import sys
sys.setrecursionlimit(1000000)

def preorder_convert(in_s, post_s, num):
    global n
    root = postorder[post_s+num-1]
    preord.append(root)
    root_id = inord_idx[root]
    lnum = root_id-in_s
    rnum = num-lnum-1
    if lnum:
        preorder_convert(in_s, post_s, lnum)
    if rnum:
        preorder_convert(root_id+1, post_s+lnum, num-lnum-1)


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
inord_idx = [0]*(n+1)
for i in range(n):
    inord_idx[inorder[i]] = i
preord = []
preorder_convert(0, 0, n)
print(*preord)
