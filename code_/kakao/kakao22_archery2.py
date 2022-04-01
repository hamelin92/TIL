def solution(n, info):
	answer = [0]*11
	apeach = 0
	lion = 0
	value = 11
	for i in range(11):
		if info[i] > 0:
			apeach += 10-i
			value *= info[i] + 1
	priority = [[i, ((2*(10-i)*value)//(1+info[i])) + i if info[i] > 0 else (10-i)*value + i] for i in range(11)]
	priority.sort(key = lambda x: x[1], reverse = True)


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))



'''
n	info	result
5	[2,1,1,1,0,0,0,0,0,0,0]	[0,2,2,0,1,0,0,0,0,0,0]
1	[1,0,0,0,0,0,0,0,0,0,0]	[-1]
9	[0,0,1,2,0,1,1,1,1,1,1]	[1,1,2,0,1,2,2,0,0,0,0]
10	[0,0,0,0,0,0,0,0,3,4,3]	[1,1,1,1,1,1,1,1,0,0,2]
'''