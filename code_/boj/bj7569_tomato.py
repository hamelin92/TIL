import sys
from collections import deque # bfs를 위한 deque 자료구조 사용
M, N, H = map(int, input().split()) # 2 <= M,N <= 100, 1 <= H <= 100
tomatos = [[list(map(int,  sys.stdin.readline().split())) for i in range(N)] for _ in range(H)] #3차원 리스트로 토마토 데이터를 받아온다.
di = [1, 0, -1, 0, 0, 0] # 가로 탐색 M 축
dj = [0, 1, 0, -1, 0, 0] # 세로 탐색 N 축
dk = [0, 0, 0, 0, 1, -1] # 상하 탐색 H 축
cnt = 0
que = deque() # deque 생성

# deque에 초기 익은 토마토 위치를 저장. 동시에 안익은 토마토 카운트
for i in range(M):
	for j in range(N):
		for k in range(H):
			if tomatos[k][j][i] == 1:
				que.append([k,j,i])
			elif tomatos[k][j][i] == 0:
				cnt += 1
day = 0
while cnt > 0:
	dif = 0 # 일일 변화량 체크 변수
	T = len(que) #하루 내에 탐색을 시도할 분량
	for t in range(T):
		x = que.popleft()
		# deque에서 첫번째 값부터 순서대로 pop하면서 탐색 진행
		for d in range(6): #가로세로 4방향 + 상하 2방향 탐색
			ni, nj, nk = x[2] + di[d], x[1] + dj[d], x[0] + dk[d]

			if 0 <= ni < M and 0 <= nj < N and 0 <= nk < H and tomatos[nk][nj][ni] == 0: # 안익은 토마토가 잇는 경우
				que.append([nk,nj,ni]) # 그 토마토는 익은 토마토가 되고 그 좌표가 다시 deque에 append 된다.
				tomatos[nk][nj][ni] = 1
				dif += 1 # 일일 변화량 + 1
	else: # for 문이 종료 되면 누적된 변화량만큼 cnt에서 빼준다 ( cnt(안익은 토마토 총 개수), dif(당일에 익은 토마토 개수))
		cnt -= dif
		if dif > 0: # for문이 종료된 상태로 변화량이 있었다는 것은 하루가 지났다는 의미
			day += 1
		else: # 변화량이 없다면 종료
			break

if cnt > 0: # 모든 루프가 끝나고 cnt>0 즉 안익은 토마토가 남아있다면 -1 출력
	print(-1)
else: # 그렇지 않다면 day 출력 ( 만약 처음부터 토마토가 다 익어 있다면 while문에 진입하지 않게 되고 day에는 0이 저장되어 있을 것이다.)
	print(day)