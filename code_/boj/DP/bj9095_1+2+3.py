dp = [1, 1, 2, 4]
T = int(input())
for t in range(T):
    N = int(input())
    while len(dp) < N+1:
        dp.append(dp[-1] + dp[-2] + dp[-3])
    print(dp[N])