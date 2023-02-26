import sys

def matmult_2(A, B, N):
    zip_b = list(zip(B))
    return [[sum([row[k]&col[0][k] for k in range(N)])%2 for col in zip_b] for row in A]



n = int(sys.stdin.readline())
K = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(matmult_2(K, K, n))
