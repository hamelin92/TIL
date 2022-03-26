from pprint import pprint
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 칸수와 진행 턴 수
    board = [[0]*N for _ in range(N)] # 오델로 판
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2 # 오델로 판 초기 세팅 (백돌)
    board[N // 2][N // 2 - 1] = board[N // 2 - 1][N // 2] = 1 # 오델로 판 초기 세팅 (흑돌)
    di = [-1, -1, 0, 1, 1, 1, 0, -1] # 8방향으로 탐색하기 위한 초기 세팅( 행 인덱스 )
    dj = [0, 1, 1, 1, 0, -1, -1, -1] # 위와 동일 ( 열 인덱스 )
    cnt = [2, 2] # 흑돌, 백돌 개수 카운트 초기값
    for turn in range(M):
        j, i, player = map(int, input().split()) # 각턴마다 열 인덱스, 행 인덱스, 흑백여부(1,2) 순서로 입력
        i = i-1 # 행과 열 인덱스는 실제로는 0부터 시작이므로 1씩 빼준다.
        j = j-1
        board[i][j] = player # 일단 해당 좌표에 해당 색의 돌을 놓는다.
        cnt[player - 1] += 1 # 해당 색의 돌 카운트 +1
        for k in range(8): # 8 방향으로 탐색
            ni = i + di[k] # 각 방향으로 좌표 이동
            nj = j + dj[k]
            if 0 <= ni < N and 0<= nj < N and board[ni][nj] != player and board[ni][nj] != 0:
                # 만약 해당 좌표가 현재 돌 색과 다른 색이고 빈칸이 아닌 경우 더 깊숙히 탐색 시작.
                check = [[ni, nj]] # 해당 방향으로 탐색 완료된 좌표를 check 리스트에 저장.
                while 0 <= ni < N and 0<= nj < N: # 탐색 좌표가 인덱스 범위 내를 벗어날 떄까지 루프 반복
                    ni += di[k] # 처음 진행한 방향으로 한칸 더 나아간다.
                    nj += dj[k]
                    if 0 <= ni < N and 0<= nj < N and board[ni][nj] == 0:
                        # 만약 그곳이 빈칸이면 루프 탈출
                        break
                    elif 0 <= ni < N and 0<= nj < N and board[ni][nj] == player:
                        # 만약 그곳이 본래 자기와 같은 색의 돌이 놓여있다면
                        for pt in check: # 기존에 탐색이 완료된 좌표를 돌면서 해당 좌표를 자기 돌로 바꿔준다.
                            board[pt[0]][pt[1]] = player
                            cnt[player-1] += 1 # 자기 돌의 카운트는 +1
                            cnt[player%2] -= 1 # 반대쪽 돌의 카운트는 -1
                        break # 루프 탈출
                    elif 0 <= ni < N and 0<= nj < N:
                        # 만약 그외에 인덱스 범위 내라면 ( 즉, 인덱스 범위 내 반대 색깔 돌을 만난 경우)
                        check.append([ni, nj]) # 탐색 리스트에 저장
                    else: #그 외의 경우 (인덱스 범위를 벗어난 경우 ) 루프 탈출
                        break
    print(f'#{tc} {cnt[0]} {cnt[1]}')

'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2

'''