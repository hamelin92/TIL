T = int(input())
for tc in range(1,T+1):
	N = int(input())
	print(f'#{tc}')
	length = 0 #문자열의 폭을 측정할 변수
	for i in range(N):
		C, num = input().split() # 출력할 문자를 입력할 변수 C와 그 개수 num 입력
		num = int(num) # num값은 int값으로 저장
		for j in range(num): # 해당 문자의 개수만큼 반복
			print(C, end='') # 해당 문자를 공백없이 출력
			length += 1 # 문자 하나 출력할 떄마다 +1
			if length == 10: # length 값이 10 인 경우 줄을 바꾸고 0으로 초기화
				print()
				length = 0
	else:
		if length > 0: #모든 반복이 끝나고 마지막에 완전하지 않게 끝났다면 마무리로 줄바꿈
			print()