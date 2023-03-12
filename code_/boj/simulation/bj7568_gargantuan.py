N = int(input())
body_info = [list(map(int, input().split())) for _ in range(N)]
res = [1] * N
for i in range(N):
    for j in range(N):
        if i != j:
            if body_info[i][0] < body_info[j][0] and body_info[i][1] < body_info[j][1]:
                res[i] += 1
print(*res)