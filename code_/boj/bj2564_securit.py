width, height = map(int, input().split())
N = int(input())
markets = [list(map(int, input().split())) for _ in range(N)] # 상점들의 위치
start = list(map(int, input().split())) # 시작지점
def position(pair): #상대적으로 표시된 상점들의 위치 정보를 절대적인 수치로 변경
	if pair[0] == 1: # 왼쪽 위 모서리를 기준으로 시계방향으로 돈 거리를 계산.
		return pair[1] #북쪽의 경우 그 값 그 자체가 좌표가 된다.
	elif pair[0] == 4: # 동쪽의 경우 너비의 길이만큼을 지나고나서 주어진 값만큼 더해진다.
		return width + pair[1]
	elif pair[0] == 2: # 남쪽의 경우 너비,높이만큼 더해지고 거기에 (너비 - 위치값)만큼 더해진다.
		return 2*width + height - pair[1]
	else: # 서쪽의 경우 너비*2에 높이만큼 더해지고 거기에 (높이-위치값)만큼 더해진다.
		return 2*width +2*height - pair[1]
def distance(pair1, pair2): # 둘 사이의 최소 거리는  둘의 절대적인 위치의 차이로 정해진다.
	# 그 차이값과 반대방향으로 체크한, 즉 블록의 둘레에서 기존 차이만큼 뺀 값을 비교해서
	# 더 작은 값이 최소 거리가 된다.
	n = abs(position(pair1)-position(pair2))
	return min(n, 2*width + 2*height - n)
result = 0
for market in markets: # 각각의 상점을 순회하면서 둘 사이의 최소 거리를 결과값에 더해준다.
	result += distance(start, market)

print(result)
