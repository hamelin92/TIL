def solution(cacheSize, cities):
	from collections import deque
	answer = 0
	cache = deque()
	for ct in cities:
		city = ct.casefold()
		for c in range(len(cache)):
			if city == cache[c]:
				for i in range(c, len(cache)-1):
					cache[i], cache[i+1] = cache[i+1], cache[i]
				answer += 1
				break
		else:
			cache.append(city)
			if len(cache) > cacheSize:
				cache.popleft()
			answer += 5
	return answer

print(solution(3, ["A","B","A"]))