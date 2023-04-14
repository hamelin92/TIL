import sys

N = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(N)]
dp = [[0]*2 for _ in range(N)]
dp[0][0] = stairs[0]
dp[0][1] = stairs[0]
if N >= 2:
    dp[1][0] = stairs[0] + stairs[1]
    dp[1][1] = stairs[1]
for i in range(2, N):
    dp[i][0] = dp[i-1][1] + stairs[i]
    dp[i][1] = max(dp[i-2]) + stairs[i]

print(max(dp[-1]))