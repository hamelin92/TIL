import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = dict(map(int, sys.stdin.readline().split()) for _ in range(N))
A_l = sorted(A.keys())
D = [0 for _ in range(len(A_l))]
X = [A[A_l[0]]]
D[0] = 1
lis = set(A.keys())
for i in range(1, len(A_l)):
    l = 1
    r = len(X)
    if X[-1] < A[A_l[i]]:
        X.append(A[A_l[i]])
        D[i] = r+1
    elif X[0] >= A[A_l[i]]:
        X[0] = A[A_l[i]]
        D[i] = 1
    else:
        l = bisect_left(X, A[A_l[i]])
        D[i] = l+1
        if X[l] > A[A_l[i]] > X[l-1]:
            X[l] = A[A_l[i]]
        
print(len(A_l)-len(X))
lis_id = len(X)
for k in range(len(A_l)-1, -1, -1):
    if D[k] == lis_id:
        lis.remove(A_l[k])
        lis_id -= 1
print(*sorted(lis), sep="\n")
