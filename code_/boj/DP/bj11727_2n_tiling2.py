n = int(input())
dp = [0]*(n+1)
dp[0], dp[1] = 1, 1
for k in range(2, n+1):
    dp[k] = (dp[k-1] + 2*dp[k-2])%10007
print(dp[-1])
