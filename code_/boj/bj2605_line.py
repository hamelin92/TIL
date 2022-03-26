N = int(input())
numbers = list(map(int, input().split()))
result = [] # 결과값을 저장할 리스트

def change(num): #받은 숫자만큼 result를 맨뒤의 원소부터 한칸씩 반복해서 자리를 바꿔주는 함수
	l = len(result)
	for i in range(num): # 맨 뒤쪽부터 차례대로 바로 앞의 원소와 위치를 바꿔주고 반복한다.
		result[l-i-1], result[l-i-2] = result[l-i-2], result[l-i-1]

for num in range(1, N+1): # 입력받은 numbers 리스트를 차례대로 순회한다.
	# 차례차례 result 리스트에 학생을 나타내는 번호를 넣는다
	result.append(num)
	# 넣은 다음 그 학생이 받은 숫자만큼 change 함수를 실행한다.
	change(numbers[num-1])

print(*result)

