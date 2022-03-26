board = []
ans = []
for _ in range(5): # 빙고판 ( 1차 리스트)
	board += list(map(int, input().split()))
for _ in range(5): # 사회자 ( 1차 리스트)
	ans += list(map(int, input().split()))

bingo_cnt = [0]*12 # 빙고 카운트 하기 위한 리스트

for num in range(25):
	idx = divmod(board.index(ans[num]), 5) #ans리스트의 값을 차례대로 board에서의 인덱스
	#빙고판 리스트를 2차리스트로 간주할 경우에 대응하는 행과 열 인덱스로 변환
	#이후 board를 2차 리스트인 것처럼 간주하고 빙고를 카운트
	bingo_cnt[idx[0]] += 1 # bingo_cnt의 0~4번째공간은 각각 n번째 행에서의 빙고를 카운트
	bingo_cnt[5+idx[1]] += 1 # 5~9번째 공간은 각각 n번쨰 열에서의 빙고를 카운트
	if idx[0] == idx[1]: # 대각선 방향에 위치할 값들을 카운트
		bingo_cnt[10] += 1
	if 4 - idx[0] == idx[1]: # 반대방향 대각선에 위치한 값들을 카운트
		bingo_cnt[11] += 1
	if bingo_cnt.count(5) >= 3: #bingo_cnt에 5라는 값이 생길때 마다 빙고 +1이다.
		print(num+1) # num은 0부터 24범위이므로 1을 더해서 출력해준다.
		break # 원하는 결과가 나왔으므로 반복문을 break문으로 탈출한다.
