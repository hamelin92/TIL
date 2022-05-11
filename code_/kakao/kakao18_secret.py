def solution(n, arr1, arr2):
	answer = []
	complete = [arr1[i]|arr2[i] for i in range(n)]
	for l in complete:
		trans = ''
		for i in range(n):
			if 2**(n-i-1)& l:
				trans += '#'
			else:
				trans += ' '
		answer.append(trans)
	return answer
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))


'''
매개변수	값
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]
매개변수	값
n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
'''