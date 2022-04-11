from math import gcd
T = int(input())
for tc in range(1, T+1):
	N = int(input())
	numbers =list(map(int, input().split()))
	total_sum = sum(numbers)
	max_gcd = 1
	for n in range(N):
		tmp_min = numbers[(n+1)%N]
		tmp_sum = total_sum - numbers[n]
		for k in range(N-1):
			tmp = gcd(tmp_sum,numbers[(n+1+k)%N])
			if tmp_min > tmp:
				tmp_min = tmp
			if tmp_min <= max_gcd:
				break
		if tmp_min > max_gcd:
			max_gcd = tmp_min
				
	print(f'#{tc} {max_gcd}')