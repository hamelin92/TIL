import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))[::-1]
X = [A[0]]
for i in range(1, N):
    l = 1
    r = len(X)
    if X[-1] < A[i]:
        X.append(A[i])
    elif X[0] >= A[i]:
        X[0] = A[i]
    else:
        l = bisect_left(X, A[i])
        if X[l] > A[i] > X[l-1]:
            X[l] = A[i]
print(len(X))
