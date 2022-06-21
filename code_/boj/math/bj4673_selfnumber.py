def generator(num):
	result = num
	while num:
		result += num%10
		num //= 10
	return result


numbers = set(range(1,10001))
noself = set()
for n in range(1,10001):
	if n in noself:
		noself.add(generator(n))
	else:
		print(n)
		noself.add(generator(n))
