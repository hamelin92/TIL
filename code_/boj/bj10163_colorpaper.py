N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
areas = [set() for _ in range(N)]
for n in range(N): #N개의 각각의 색종이에 대해
    for i in range(papers[n][2]): #시작점 기준으로 너비, 높이에 따라
        for j in range(papers[n][3]): #격자(넓이1)의 좌표를 따로 set에 저장.
            areas[n].add((papers[n][0]+i, papers[n][1]+j))
unions =set() | areas[N-1] # 가장 최신의 색종이부터 거슬러 올라가면서
# 누적되는 가려지는 부분을 나타낼 집합
for n in range(N-1):
    areas[N-n-2] = areas[N-n-2] - unions # 위부터 내려가면서 가려지는 부분 제거
    unions |= areas[N-n-2] # 가려지는 부분은 점점 더해짐
for n in range(N):
    print(len(areas[n]))

