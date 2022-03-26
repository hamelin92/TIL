N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
grid = [[0]*1001 for _ in range(1001)]
areas = [0]*N
for n in range(N-1, -1, -1): #N개의 각각의 색종이에 대해 ( 위에서 부터 )
    for i in range(papers[n][2]): #시작점 기준으로 너비, 높이에 따라
        for j in range(papers[n][3]): #격자(넓이1)의 좌표를 따라 그리드에 1 저장
            if grid[papers[n][0]+i][papers[n][1]+j] == 0: # (해당 좌표가 0이면)
                grid[papers[n][0] + i][papers[n][1] + j] = 1
                areas[n] += 1 #그떄마다 n번 색종이의 넓이 +1

for n in range(N):
    print(areas[n])
