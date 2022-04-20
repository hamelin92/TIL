from pprint import pprint


paper = [list(map(int, input().split())) for _ in range(10)]
size = [0, 5, 5, 5, 5, 5]
newpaper = [[0]*10 for _ in range(10)]
def square_chk(y,x):
	max_s = 0
	for i in range(5):
		if y+i < 10 and x+i < 10 and paper[y+i][x+i] == 1:
			for j in range(1,i+1):
				if paper[y+i-j][x+i] == 1 and paper[y+i][x+i-j] == 1:
					continue
				else:
					return max_s
			else:
				max_s = i+1
	return max_s

for i in range(10):
	for j in range(10):
		newpaper[i][j] = square_chk(i,j)
		if newpaper[i][j] == 5:
pprint(newpaper)
