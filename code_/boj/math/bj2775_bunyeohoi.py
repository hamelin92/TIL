
apart = [[j for j in range(1, 15)] for _ in range(15)]
for i in range(1, 15):
    for j in range(1, 14):
        apart[i][j] = apart[i][j-1] + apart[i-1][j]
T = int(input())
for t in range(T):
    k = int(input()) # 층
    n = int(input()) # 호
    print(apart[k][n-1])