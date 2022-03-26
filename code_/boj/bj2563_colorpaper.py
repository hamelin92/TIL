N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
# 색종이의 위치 정보를 담은 2차리스트로 입력을 받는다.
grid = [[0]*100 for _ in range(100)] # 2차 리스트로 그리드를 만들어준다.

cnt = 0 # 넓이를 계산할 카운트
for paper in papers: #각각의 색종이에 대해 순회
	for i in range(10): #색종이 내부의 격자 순회 (x 좌표에 따라)
		for j in range(10): # y좌표
			if grid[paper[0]+i][paper[1]+j] == 0: # 해당 좌표의 그리드 값이 0이면
				grid[paper[0] + i][paper[1] + j] = 1 # 1로 바꿔준다.
				cnt += 1 #카운트 +1

print(cnt)