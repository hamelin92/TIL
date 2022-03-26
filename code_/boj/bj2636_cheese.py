from collections import deque
N, M = map(int, input().split())
cheeses = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
di = [0, 1, 0, -1] # 델타 탐색을 위한 리스트
dj = [1, 0, -1, 0]
start = [[0,0], [N-1, M-1], [0, M-1], [N-1, 0]]
visit[0][0] = visit[N-1][M-1] = visit[0][M-1] = visit[N-1][0] = 1 # 4방향 외곽 모서리부터 탐색 시작
que = deque(start) # 치즈 외곽을 탐색하기 위한 큐
cheese_que = deque([]) # 녹게될 치즈 위치를 담을 큐
times = 0
cnt = 0
while que or cheese_que: # 두 종류의 큐가 모두 빌 떄까지 반복
    check = 0 # 치즈 유무 확인용 변수, 전체 반복마다 ( 매 반복이 1시간과 같다) 0으로 초기화
    while que: #치즈의 표면을 만날떄까지 큐를 돌면서 탐색 반복 ( bfs )
        v = que.popleft()
        for d in range(4):
            ni = v[0] + di[d]
            nj = v[1] + dj[d]
            if 0 <= ni < N and 0 <= nj < M and visit[ni][nj] == 0: # 인덱스 범위 내에서 방문 기록이 없는 경우
                visit[ni][nj] = 1 # 방문 기록
                if cheeses[ni][nj] == 0: # 치즈가 아닌 경우는 일반 큐에 넣는다.
                    que.append([ni,nj])
                else: # 치즈의 경우는 치즈 큐에 넣는다.
                    cheese_que.append([ni, nj])
    else:
        if len(cheese_que) > 0: # 반복이 종료되고 (치즈 외곽의 가능한 위치는 전부 탐색 완료 상태)
            # 치즈 큐에 원소가 들어있는 경우 cnt에 그 길이를 저장. ( 0이 되는 순간은 저장이 되지 않기 때문에 마지막 순간 사라지기 직전을 기록한다)
            cnt = len(cheese_que)
    while cheese_que: # 이번에는 치즈 큐를 돌면서 치즈 칸을 일반칸으로 바꿔 녹았다는 것을 표현한다.
        # 녹을 치즈가 존재했다는걸 확인하기위해 check 변수에 1을 할당하고 바꿔진 칸은 일반 큐에 다시 넣어준다.
        check = 1
        ch_v = cheese_que.popleft()
        que.append(ch_v)
        cheeses[ch_v[0]][ch_v[1]] = 0
    else: # 반복이 끝나고 check 변수가 1이라면 times +1. 치즈가 녹는 액션이 존재하는 경우에만 시간 변수가 올라간다.
        if check == 1:
            times += 1
print(times)
print(cnt)
'''
3 3
0 0 0
0 0 0
0 0 0
'''
