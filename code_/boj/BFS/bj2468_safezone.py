from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]
max_height= 1
for i in range(N):
    for j in range(N):
        if max_height < heights[i][j]:
            max_height = heights[i][j]
ans = 1
for k in range(1, max_height): # k : 강수량 높이
    ans_k = 0
    visit = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if heights[i][j] <= k:
                heights[i][j] = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and heights[i][j] > 0:
                ans_k += 1
                que = deque([[i,j]])
                visit[i][j] = 1
                while que:
                    q = que.popleft()
                    for direction in range(4):
                        ni = q[0] + di[direction]
                        nj = q[1] + dj[direction]
                        if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and heights[ni][nj] > 0:
                            que.append([ni, nj])
                            visit[ni][nj] = 1
    if ans_k > ans:
        ans = ans_k
print(ans)
    

