from pprint import pprint

info = [list(map(int, input().split())) for _ in range(4)]
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, -1, -1, -1, 0, 1, 1, 1]
newinfo = [[[info[i][2*j], info[i][2*j+1]-1] for j in range(4)] for i in range(4)]
shark =[0,0,0]
dic= {}
for i in range(4):
	for j in range(4):
		dic[newinfo[i][j][0]] = [i,j]
fish = set(range(1,17))
shark[2] = newinfo[0][0][1]
fish.remove(newinfo[0][0][0])
newinfo[0][0] = [0,0]
max_value = 0

def shark_move(y,x,d,fishes,score, inf):
	global max_value
	if score > max_value:
		max_value = score
	if len(fishes) == 0:
		if score > max_value:
			max_value = score
		return
	for n in range(1,17):
		if n in fishes:
			flag = 0
			for i in range(4):
				for j in range(4):
					if inf[i][j][0] == n:
						n_f = [i, j]
						flag = 1
						break
				if flag == 1:
					break

			for k in range(8):
				newdir = (k + inf[n_f[0]][n_f[1]][1]) % 8
				ni = n_f[0] + di[newdir]
				nj = n_f[1] + dj[newdir]
				if 0 <= ni < 4 and 0 <= nj < 4 and (ni,nj) != (shark[0],shark[1]):
					inf[n_f[0]][n_f[1]][1] = newdir
					inf[n_f[0]][n_f[1]], inf[ni][nj] = inf[ni][nj], inf[n_f[0]][n_f[1]]
					break

	for k in range(1,4):
		ny = y + k * di[d]
		nx = x + k * dj[d]
		if 0 <= ny < 4 and 0 <= nx < 4 and inf[ny][nx][0] > 0:
			fish_no = inf[ny][nx][0]
			fish_dir = inf[ny][nx][1]
			inf[ny][nx] = [0, 0]
			fishes.remove(fish_no)
			shark_move(ny,nx, fish_dir ,fishes,score + fish_no, inf)
			inf[ny][nx] = [fish_no, fish_dir]
			fishes.add(fish_no)
shark_move(0,0,shark[2], fish ,newinfo[0][0][0], newinfo)
print(max_value)










