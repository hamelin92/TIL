N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for n in nums:
	if n == 1:
		continue
	elif n == 2:
		cnt += 1
		continue
	elif n == 3:
		cnt += 1
		continue
	else:
		if n%2 == 0 or n%3 == 0:
			continue
		else:
			flag = 0
			k = 5
			i = 1
			while k < 1+n**0.5:
				if n%k == 0:
					flag = 1
					break
				i += 1
				k += 2 + 2*(i%2)
			if flag == 0:
				cnt += 1
print(cnt)
