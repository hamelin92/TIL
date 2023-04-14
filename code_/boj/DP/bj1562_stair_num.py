from collections import defaultdict

N = int(input())
dp = defaultdict(int)
ans = 0
for i in range(1, 10):
    dp[tuple([i==j for j in range(10)] + [i])] += 1
for i in range(1, N):
    ith = []
    for key in dp.keys():
        if key[-1] > 0:
            nkey = list(key)
            nkey[-1] -= 1
            nkey[key[-1]-1] = True
            ith.append([nkey, dp[key]])
        if key[-1] < 9:
            nkey = list(key)
            nkey[-1] += 1
            nkey[key[-1]+1] = True
            ith.append([nkey, dp[key]])
    for key in dp.keys():
        dp[key] = 0
    for nn in ith:
        dp[tuple(nn[0])] += nn[1]
for k in range(10):
    ans += dp[(True, True, True, True, True, True, True, True, True, True, k)]
print(ans%1000000000)