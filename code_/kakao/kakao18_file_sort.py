def solution(files):
	from collections import defaultdict
	answer = []
	dic = defaultdict(list)
	for i in range(len(files)):
		file = files[i]
		head = ''
		number = ''
		flag = 0
		for f in file:
			if f.isnumeric():
				number += f
				flag = 1
			elif flag == 1:
				break
			else:
				head += f.lower()
		dic[(head, int(number))].append(file)
	sorted_key = sorted(dic.keys())
	for s in sorted_key:
		answer.extend(dic[s])
	print(answer)
	return answer

solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])

'''
["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
'''