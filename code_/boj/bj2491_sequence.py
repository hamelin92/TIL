N = int(input())
seq = list(map(int, input().split())) #수열을 입력하는 리스트
cnt = tmp_cnt = max_cnt = 1 #전체 길이, 값이 같은 경우를 위한 임시 변수, 최대길이를 저장할 변수
chk = 1 # 연속적인 증감 상태를 체크하기 위한 변수(1: 증가, -1: 감소)
# 시작, 끝값을 전부 카운트하는 길이이므로 길이 관련 변수의 default 값은 1로 설정.
for num in range(1, N): #수열의 2번째 값부터 시작.
	if seq[num] > seq[num-1] and chk == 1: #증가상태이면서 확실히 증가했을 경우 카운트 +1
		cnt += 1
		tmp_cnt = 1 # 값이 변했으므로 tmp값 초기화
	elif seq[num] < seq[num-1] and chk == -1: # 감소상태이면서 확실히 감소했을 경우 카운트 +1
		cnt += 1
		tmp_cnt = 1 # 값이 변했으므로 tmp값 초기화
	elif seq[num] == seq[num-1]: # 증감상태와 상관없이 값이 유지되는 경우 카운트 +1, 임시변수 +1
		cnt += 1
		tmp_cnt += 1
	else: # 그외의 경우, 즉 증감상태가 변한 경우 chk 변수에 -1을 곱해서 증감상태 변경.
		if max_cnt < cnt: #만약 현재까지 기록된 카운트값이 max_cnt값보다 큰 경우 갱신
			max_cnt = cnt
		cnt = tmp_cnt +1 #증감상태가 변한 경우 임시변수 + 1로 카운트 저장
		# 증감상태가 변하기 전에 연속으로 같은 값이 있는 경우 증감이 바뀔때도 그 부분이 포함되기 때문
		tmp_cnt = 1 # 증감이 바뀌었다는 것은 수열이 이전의 값과 달라졌다는 것
		# 그러므로 연속적으로 값이 같은 경우를 기록하는 tmp값은 1로 초기화한다.
		chk *= -1 # 증감상태는 -1을 곱해서 토글해준다.
else: # 빈복문이 끝난 상황에서 카운트 값을 다시 확인해서 최대값을 갱신한다.
	if max_cnt < cnt:
		max_cnt = cnt
print(max_cnt)

next