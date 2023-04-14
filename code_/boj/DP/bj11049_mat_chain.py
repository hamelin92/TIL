import sys

N = int(sys.stdin.readline())
chains = list(map(int, sys.stdin.readline().split()))+[int(sys.stdin.readline().split()[-1]) for _ in range(N-1)]
ub = sys.maxsize
dp = [[-1]*N for _ in range(N)]

def mat_chain(p, i, j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = ub
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], mat_chain(p, i, k) + mat_chain(p, k+1, j)+ p[i-1]*p[k]*p[j])
    return dp[i][j]

def chain_order(p, n):
    i = 0
    j = n-1
    return mat_chain(p, i, j)

print(chain_order(chains, N))