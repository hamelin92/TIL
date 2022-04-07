T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    park = [list(map(int, input().split())) for _ in range(N)]
    start = []
    max_h = park[0][0]
    for i in range(N):
        for j in range(N):
            if park[i][j] > max_h:
                start = [(i,j)]
            elif park[i][j] == max_h:
                start.append((i,j))
