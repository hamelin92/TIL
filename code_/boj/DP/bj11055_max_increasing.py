import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
D = A[:]
for i in range(N):
    for j in range(i):
        if A[i] > A[j] and D[i] < A[i] + D[j]:
            D[i] = A[i] + D[j]
print(max(D))