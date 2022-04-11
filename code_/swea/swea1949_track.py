
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    park = [list(map(int, input().split())) for _ in range(N)]
    start = []
    max_h = park[0][0]
    for i in range(N):
        for j in range(N):
            if park[i][j] > max_h:
                max_h = park[i][j]
                start = [(i, j)]
            elif park[i][j] == max_h:
                start.append((i, j))
    longest = 0
    for r in range(N):
        for c in range(N):
            for k in range(1, K+1):
                park[r][c] -= 1
                for s in start:
                    if s == (r,c):
                        continue
                    else:
                        stack=[s]
                        visit = [[0]*N for _ in range(N)]
                        visit[s[0]][s[1]] = 1
                        while stack:
                            v = stack[-1]
                            for d in range(4):
                                ni = v[0] + di[d]
                                nj = v[1] + dj[d]
                                if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] <= visit[v[0]][v[1]] and park[ni][nj] < park[v[0]][v[1]]:
                                    stack.append((ni,nj))
                                    visit[ni][nj] = visit[v[0]][v[1]] + 1
                                    if visit[ni][nj] > longest:
                                        longest = visit[ni][nj]
                                    break
                            else:
                                stack.pop()
            park[r][c] += K
    print(f'#{tc} {longest}')