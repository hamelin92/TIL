from pprint import pprint

def solution(m, n, board):
	answer = 0
	board = [list(board[_]) for _ in range(m)]
	flag = True

	while flag:
		flag = False
		four = set()
		for i in range(m-1):
			for j in range(n-1):
				if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
					flag = True
					four.add((i,j))
		for b in four:
			if board[b[0]][b[1]] != 0:
				board[b[0]][b[1]] = 0
				answer += 1
			if board[b[0]+1][b[1]] != 0:
				board[b[0]+1][b[1]] = 0
				answer += 1
			if board[b[0]][b[1]+1] != 0:
				board[b[0]][b[1]+1] = 0
				answer += 1
			if board[b[0]+1][b[1]+1] != 0:
				board[b[0]+1][b[1]+1] = 0
				answer += 1
		for i in range(1,m):
			for j in range(n):
				if board[i][j] == 0:
					for k in range(i,0,-1):
						board[k][j] = board[k-1][j]
					board[0][j] = 0
	return answer

print(solution(8, 5, ["HGNHU", "CRSHV", "UKHVL", "MJHQB", "GSHOT", "MQMJJ", "AGJKK", "QULKK"]))

'''
m	n	board	answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
'''