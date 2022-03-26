T = int(input())
for tc in range(1,T+1):
	N = int(input())
	result = '' # 결과를 출력하기 위한 빈 문자열 변수
	print(f'#{tc}')
	for i in range(N):
		C, num = input().split() # 출력할 문자를 입력할 변수 C와 그 개수 num 입력
		num = int(num) # num값은 int값으로 저장
		while num > 0: # num값이 0보다 큰 경우 while문 실행
			tmp = 10 - len(result) # result 문자열 (최대 10글자)에 더 채워질 수 있는 문자 수
			if tmp >= num: # num 값이 tmp 이하면 num만큼 문자를 result에 넣고 num=0d을 저장 (즉 while문 종료)
				result += C * num
				num = 0
			else:  # 그외의 경우, 즉 num값이 tmp보다 큰 경우
				# 다시 말하면 result에 더해서 한줄에 출력해야할 문자 C의 개수가 빈 칸보다 많은 경우이다.
				result += C * tmp
				num -= tmp
			if len(result) >= 10: #while문 내에서 result 문자열의 길이가 10 이상이면 출력하고 result 초기화
				print(result)
				result = ''
	else: # for문이 종료되고 10글자가 채워지지 않아 출력하지 못한 문자열이 남았다면 그것을 출력한다.
		if len(result) > 0:
			print(result)